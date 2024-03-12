import pandas as pd

class DataProcessor():
    """
    Loads and cleans data from the relevant .csv file.
    """
    def __init__(self, filepath:str) -> None:
        self.df_training_raw = self.load_csv(filepath)
        self.df_training_clean = self.clean_df()
        self.df_training_extended = self.calculate_profit_per_headcount()
    
    def load_csv(self, filepath:str):
        """
        Load the CSV data into a Pandas dataframe.
        Returns: Pandas dataframe
        """
        try:
            df = pd.read_csv(filepath, header=0, skip_blank_lines=True, skipinitialspace=True).dropna(how='all')
            return df
        
        except KeyError:
            raise KeyError(f"Couldn't find data file {filepath}")
    
    def clean_df(self):
        """
        Cleans the data from the CSV.
        Returns: Cleaned Pandas dataframe
        """
        df = self.df_training_raw
        
        # Delete first column (i.e. counter)
        df.drop(df.columns[0], axis=1, inplace= True)
        
        # Cast column data types
        df['site'] = df['site'].astype(str)
        df['sales'] = df['sales'].round(decimals=2)
        df['period_of_day'] = df['period_of_day'].astype(str)
        df['headcount'] = df['headcount'].astype(int)

        return df
    
    def calculate_profit_per_headcount(self):
        """
        Calculates the average profit per staff member. 
        Profit is simplified as sales minus tax and salaries.
        
        Assumptions: 
        - Tax rate is 20%
        - Salary is £11.95 per staff member (London living wage 2022-2023).
        """
        df_extended = self.df_training_clean
        
        # Calculate taxes and costs
        df_extended["sales_taxes"] = df_extended["sales"] * 0.2
        df_extended["labour_costs"] = df_extended["headcount"] * 11.95
        
        # Calculate profits
        df_extended["total_profit"] = df_extended["sales"] - (df_extended["sales_taxes"] + df_extended["labour_costs"])
        df_extended["avg_profit_per_headcount"] = df_extended["total_profit"] / df_extended["headcount"]
                    
        return df_extended

    def describe_df_column(self, column:str):
        print(self.df_training_extended.groupby(['site','period_of_day'])[column].describe())

import pandas as pd

class DataProcessor():
    """
    Loads and cleans data from the relevant .csv file.
    """
    def __init__(self, filepath:str) -> None:
        self.df_training_raw = self.load_csv(filepath)
        self.df_training_clean = self.clean_df()
    
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
        
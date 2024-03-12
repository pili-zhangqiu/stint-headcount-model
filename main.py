from data_processor import DataProcessor
from data_plotter import DataPlotter

if __name__ == '__main__':
    # Setup - Load and clean data
    data_processor = DataProcessor('sites_data.csv')
    data = data_processor.df_training_extended

    # Explore the data - Plots
    # Describe
    data_processor.describe_df_column("sales")
    data_processor.describe_df_column("total_profit")
    data_processor.describe_df_column("avg_profit_per_headcount")

    # Plot
    plotter = DataPlotter(data)
    plotter.plot_all()
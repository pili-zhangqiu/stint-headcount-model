from data_processor import DataProcessor
from data_plotter import DataPlotter

if __name__ == '__main__':
    # Setup - Load and clean data
    data_processor = DataProcessor('sites_data.csv')

    # Explore the data - Plots
    # Describe and plot all values
    data = data_processor.df_training_extended
    print(data.head(100))
    
    data_processor.describe_df_column("sales")
    data_processor.describe_df_column("total_profit")
    data_processor.describe_df_column("avg_profit_per_headcount")

    plotter = DataPlotter(data)
    plotter.plot_all()

    # Plot only values with optimal profitability
    data_optimal_prof = data_processor.df_training_optimal_prof
    
    print(data_optimal_prof.head(100))
    print(f"{len(data_optimal_prof)} passed the 40 GBP/staff criteria for optimal headcount.")
    
    plotter_prof = DataPlotter(data_optimal_prof)
    plotter_prof.plot_all()
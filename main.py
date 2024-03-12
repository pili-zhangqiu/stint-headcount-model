from data_processor import DataProcessor
from data_plotter import DataPlotter
from model_optimal_headcount import ModelOptimalHeadcount


if __name__ == '__main__':
    # ----- Setup - Load and clean data -----
    data_processor = DataProcessor('sites_data.csv')

    # ----- Explore the data - Plots -----
    # Describe and plot all values
    print("\n----- Extended Data - All Profitabilities -----")
    data = data_processor.df_training_extended
    print("\nAll data")
    print(data.head(100))
    
    data_processor.describe_df_column("sales")
    data_processor.describe_df_column("total_profit")
    data_processor.describe_df_column("avg_profit_per_headcount")

    plotter = DataPlotter(data)
    #plotter.plot_all()

    # Plot only values with optimal profitability
    print("\n----- Extended Data - Optimal Profitabilities -----")
    data_optimal_prof = data_processor.df_training_optimal_prof
    
    print("Optimal profit data")
    print(data_optimal_prof.head(100))
    print(f"  -> {data_optimal_prof.shape[0]} passed the 40 GBP/staff criteria for optimal headcount.")
    
    plotter_prof = DataPlotter(data_optimal_prof)
    #plotter_prof.plot_all()
    
    # ----- Model -----
    print("\n----- Model -----")
    rf_model = ModelOptimalHeadcount(data_optimal_prof, print_tree=False, show_cm=False, show_pred=True)
    
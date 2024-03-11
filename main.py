from data_processor import DataProcessor
from data_plotter import DataPlotter

if __name__ == '__main__':
    # Setup - Load and clean data
    data_processor = DataProcessor('sites_data.csv')
    data = data_processor.df_training_clean

    # Explore the data - Plots
    plotter = DataPlotter(data)
    
    plotter.scatterplot_headcount_vs_sales_per_site()
    plotter.scatterplot_headcount_vs_sales_per_site_period("morning")
    plotter.scatterplot_headcount_vs_sales_per_site_period("afternoon")
    plotter.scatterplot_headcount_vs_sales_per_site_period("evening")
    
    plotter.boxplot_headcount_per_site_period()
    plotter.boxplot_sales_per_site_period_a()
    plotter.boxplot_sales_per_site_period_b()

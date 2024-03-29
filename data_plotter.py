import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import seaborn as sns

import os

class DataPlotter:
    def __init__(self, df:pd.DataFrame) -> None:
        self.df_training = df
        
    def plot_all(self):
        """
        Plots all relevant graphs.
        """
        # Scatter plots
        self.scatterplot_headcount_vs_sales_per_site()
        self.scatterplot_headcount_vs_sales_per_site_period("morning")
        self.scatterplot_headcount_vs_sales_per_site_period("afternoon")
        self.scatterplot_headcount_vs_sales_per_site_period("evening")
        
        # Box plots
        self.boxplot_headcount_per_site_period()
        self.boxplot_sales_per_site_period_a()
        self.boxplot_sales_per_site_period_b()

        # Violin plots
        self.violinplot_sales_per_site_period()
        self.violinplot_per_site_period(x="site", y="avg_profit_per_headcount", hue="period_of_day")

    def scatterplot_headcount_vs_sales_per_site(self):
        """
        Scatered plot showing relationship between headcount and sales.
        Grouped by site.
        """
        df = self.df_training
        
        df_site_1 = df[df["site"] == 'site1']
        df_site_2 = df[df["site"] == 'site2']
        df_site_3 = df[df["site"] == 'site3']
        df_site_4 = df[df["site"] == 'site4']
        df_sites = [df_site_1, df_site_2, df_site_3, df_site_4]
        
        # Plots
        fig = plt.figure()
        splot = fig.add_subplot(111)
        site_counter = 1
        
        for site in df_sites:
            splot.scatter(site['sales'], site['headcount'], 
                        s = 200, alpha=0.2, edgecolors = 'black', label=f'Site {site_counter}')
            site_counter += 1
        
        plt.yticks(np.arange(min(df['headcount']), max(df['headcount'])+1, 1.0))
        plt.title('Headcount vs sales\n(grouped by sites)', loc='center')
        plt.xlabel('Sales (£)', loc='center')
        plt.ylabel('Headcount', loc='center')
        lgd = plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
        
        # Save plot
        if not os.path.exists("plots"):
            os.makedirs("plots")
        plt.savefig(fname="plots/scatterplot_headcount_vs_sales_per_site", bbox_extra_artists=(lgd,), bbox_inches='tight')
        
    def scatterplot_headcount_vs_sales_per_site_period(self, period_of_day:str):
        df = self.df_training
        try:
            df_site_1 = df[(df["site"] == 'site1') & (df["period_of_day"] == period_of_day)]
            df_site_2 = df[(df["site"] == 'site2') & (df["period_of_day"] == period_of_day)]
            df_site_3 = df[(df["site"] == 'site3') & (df["period_of_day"] == period_of_day)]
            df_site_4 = df[(df["site"] == 'site4') & (df["period_of_day"] == period_of_day)]
            df_sites = [df_site_1, df_site_2, df_site_3, df_site_4]
        except KeyError:
            raise KeyError("Cannot find specified period of day in the database.")
        
        # Plots
        site_counter = 1
        fig = plt.figure()
        splot = fig.add_subplot(111)
        for site in df_sites:
            site_counter += 1
            splot.scatter(site['sales'], site['headcount'], 
                        s = 200, alpha=0.1, edgecolors = 'black', label=f'Site {site_counter}')
        
        plt.yticks(np.arange(min(df['headcount']), max(df['headcount'])+1, 1.0))
        plt.title(f'Headcount vs sales\n({period_of_day})', loc='center')
        plt.xlabel('Sales (£)', loc='center')
        plt.ylabel('Headcount', loc='center')
        lgd = plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
        
        # Save plot
        if not os.path.exists("plots"):
            os.makedirs("plots")
        plt.savefig(fname=f"plots/scatterplot_headcount_vs_sales_per_site_{period_of_day}", bbox_extra_artists=(lgd,), bbox_inches='tight')
        
    def boxplot_headcount_per_site_period(self):
        """
        Box plot showing headcount.
        Grouped by site.
        """
        df = self.df_training
        
        # Plots
        fig = plt.figure()
        sns.boxplot(x="period_of_day",
            y="headcount",
            hue="site",
            data=df,
            palette="rocket", 
            notch=True, showcaps=False,
            medianprops={"color": "r", "linewidth": 2},
            flierprops={"marker": "x"},
            gap=.1)
                
        plt.yticks(np.arange(min(df['headcount']), max(df['headcount'])+1, 1.0))
        plt.title('Headcount\n(grouped by sites and periods of day)', loc='center')
        plt.xlabel('Period of Day', loc='center')
        plt.ylabel('Headcount', loc='center')
        lgd = plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

        # Save plot
        if not os.path.exists("plots"):
            os.makedirs("plots")
        plt.savefig(fname="plots/boxplot_headcount_per_site_period", bbox_extra_artists=(lgd,), bbox_inches='tight')
        
    
    def boxplot_sales_per_site_period_a(self):
        """
        Box plot showing sales.
        Grouped by site and period.
        """
        df = self.df_training
        
        # Plots
        fig = plt.figure()
        sns.boxplot(x="period_of_day",
            y="sales",
            hue="site",
            data=df,
            palette="rocket", 
            notch=True, showcaps=False,
            medianprops={"color": "black", "linewidth": 1},
            flierprops={"marker": "x"},
            gap=.1)
            
        plt.title('Sales\n(grouped by sites and periods of day)', loc='center')
        plt.xlabel('Period of Day', loc='center')
        plt.ylabel('Sales (£)', loc='center')
        lgd = plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
        
        # Save plot
        if not os.path.exists("plots"):
            os.makedirs("plots")
        plt.savefig(fname="plots/boxplot_sales_per_site_period_a", bbox_extra_artists=(lgd,), bbox_inches='tight')
    
    def boxplot_sales_per_site_period_b(self):
        """
        Box plot showing sales.
        Grouped by site and period.
        """
        df = self.df_training
        
        # Plots
        fig = plt.figure()
        sns.boxplot(x="site",
            y="sales",
            hue="period_of_day",
            data=df,
            palette="rocket", 
            notch=True, showcaps=False,
            medianprops={"color": "black", "linewidth": 1},
            flierprops={"marker": "x"},
            gap=.1)

        plt.title('Sales\n(grouped by sites and periods of day)', loc='center')
        plt.xlabel('Period of Day', loc='center')
        plt.ylabel('Sales (£)', loc='center')
        lgd = plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
        
        # Save plot
        if not os.path.exists("plots"):
            os.makedirs("plots")
        plt.savefig(fname="plots/boxplot_sales_per_site_period_b", bbox_extra_artists=(lgd,), bbox_inches='tight')
       
    def violinplot_sales_per_site_period(self):
        df = self.df_training

        fig = plt.figure()
        sns.violinplot(x="site", y="sales", hue="period_of_day", data=df, palette="rocket")
        
        plt.title('Sales\n(grouped by sites and periods of day)', loc='center')
        plt.xlabel('Site', loc='center')
        plt.ylabel('Sales (£)', loc='center')
        lgd = plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
        
        # Save plot
        if not os.path.exists("plots"):
            os.makedirs("plots")
        plt.savefig(fname="plots/violinplot_sales_per_site_period", bbox_extra_artists=(lgd,), bbox_inches='tight')
    
    def violinplot_per_site_period(self, x:str, y:str, hue:str):
        df = self.df_training

        fig = plt.figure()
        sns.violinplot(x=x, y=y, hue=hue, data=df, palette="rocket")
        
        plt.title(f'{y.replace("_", " ")}\n(grouped by {x.replace("_", " ")} and {hue.replace("_", " ")})', loc='center')
        plt.xlabel(f'{x.replace("_", " ")}', loc='center')
        plt.ylabel(f'{y.replace("_", " ")} (£)', loc='center')
        lgd = plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
        
        # Save plot
        if not os.path.exists("plots"):
            os.makedirs("plots")
        plt.savefig(fname=f"plots/violinplot_{y}_per_{x}_{hue}", bbox_extra_artists=(lgd,), bbox_inches='tight')
    
# Data Processing
import pandas as pd
import numpy as np

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, ConfusionMatrixDisplay
from sklearn.model_selection import RandomizedSearchCV, train_test_split
from scipy.stats import randint

from sklearn.tree import export_graphviz, plot_tree
from IPython.display import Image, display
import graphviz
import pydot

class ModelOptimalHeadcount:
    def __init__(self, df:pd.DataFrame, print_tree=False) -> None:
        self.df_training = df
        self.model = self.rf_model(print_tree)
        
    def rf_model(self, print_tree) -> int:
        """
        Using: Random Forest Regressor model.
        Returns optimal headcount number for a specified site and period of the day.
        """
        df = self.df_training
        
        # Convert categorical data to integers
        site_to_num = {
            'site1':1,
            'site2':2,
            'site3':3,
            'site4':4
        }
        num_to_site = {
            1:'site1',
            2:'site2',
            3:'site3',
            4:'site4'
        }
        df['site'] = df['site'].map(site_to_num)

        period_of_day_to_num = {
            'morning':1,
            'afternoon':2,
            'evening':3
        }
        num_to_period_of_day = {
            1:'morning',
            2:'afternoon',
            3:'evening'
        }
        df['period_of_day'] = df['period_of_day'].map(period_of_day_to_num)

        # Features (X) and target variable (y)
        X = df.drop(['headcount', 'sales_taxes', 'labour_costs', 'total_profit', 'avg_profit_per_headcount', 'profitability'], axis=1)     # Features
        y = df['headcount']

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Fit model
        rf = RandomForestClassifier()
        rf.fit(X_train, y_train)
    
        # Prediction
        y_pred = rf.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        print("Accuracy:", accuracy)

        if print_tree:
            for i in range(4):
                tree = rf.estimators_[i]
                dot_data = export_graphviz(tree,
                                        feature_names=X_train.columns,  
                                        filled=True,  
                                        max_depth=2, 
                                        impurity=False, 
                                        proportion=True)
                graph = graphviz.Source(dot_data)
                print("---")
                display(graph)

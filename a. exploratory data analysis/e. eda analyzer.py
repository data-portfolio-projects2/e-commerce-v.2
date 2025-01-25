import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class EDAAnalyzer:
    def __init__(self, dataframe):
        self.df = dataframe
    
    def plot_boxplots(self, numerical_cols):
        for col in numerical_cols:
            plt.figure(figsize=(12, 6))
            plt.subplot(1, 2, 2)
            sns.boxplot(y=self.df[col])
            plt.title(f'{col} boxplot')
            plt.show()
    
    def calculate_skewness_kurtosis(self, numerical_cols):
        skewness = self.df[numerical_cols].skew()
        kurtosis = self.df[numerical_cols].kurtosis()
        return skewness, kurtosis
    
    def display_descriptive_statistics(self, numerical_cols):
        return self.df[numerical_cols].describe()
    
    def plot_categorical_counts(self, categorical_cols):
        for col in categorical_cols:
            plt.figure(figsize=(12, 6))
            order = self.df[col].value_counts().index
            sns.countplot(y=col, data=self.df, order=order, palette='viridis')
            plt.xlabel('total count')
            plt.ylabel(col)
            plt.show()
    
    def plot_sales_by_category(self, categorical_cols):
        for col in categorical_cols:
            order = self.df.groupby(col)['total_sales'].sum().sort_values(ascending=False).index
            plt.figure(figsize=(10, 6))
            sns.barplot(x='total_sales', y=col, data=self.df, estimator=sum, errorbar=None, palette='viridis', order=order)
            plt.xlabel('total sales')
            plt.ylabel(col)
            plt.show()
    
    def plot_correlation_matrix(self, numerical_cols):
        corr = self.df[numerical_cols].corr()
        plt.figure(figsize=(10, 8))
        sns.heatmap(corr, annot=True, linewidths=.5, cmap='coolwarm')
        plt.title('correlation matrix')
        plt.show()

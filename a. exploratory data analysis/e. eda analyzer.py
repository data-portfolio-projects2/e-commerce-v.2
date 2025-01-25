import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf

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

class EDAAnalyzer:
    def __init__(self, dataframe):
        self.df = dataframe
    
    def plot_pair_grid(self, numerical_cols):
        g = sns.PairGrid(self.df[numerical_cols])
        g.map_upper(sns.regplot, scatter_kws={'s': 10}, line_kws={'color': 'red'})
        g.map_lower(sns.regplot, scatter_kws={'s': 10}, line_kws={'color': 'red'})
        g.map_diag(sns.histplot)
        plt.suptitle('Linear Regression Pair Plot', y=1.02)
        plt.show()
    
    def perform_linear_regression(self, numerical_cols):
        for i in range(len(numerical_cols)):
            for j in range(i + 1, len(numerical_cols)):
                x_col = numerical_cols[i]
                y_col = numerical_cols[j]
                X = self.df[x_col]
                Y = self.df[y_col]
                X = sm.add_constant(X)
                model = sm.OLS(Y, X).fit()
                print(f"Linear Regression Results: {y_col} vs {x_col}")
                print(model.summary())
                print("\n" + "="*50 + "\n")
    
    def create_qqplots(self, numerical_cols):
        for i, col1 in enumerate(numerical_cols):
            for j, col2 in enumerate(numerical_cols):
                if i != j:
                    formula = f'{col1} ~ {col2}'
                    model = smf.ols(formula, data=self.df).fit()
                    residuals = model.resid
                    sm.qqplot(residuals, line='45')
                    plt.title(f'{col1} vs {col2}')
                    plt.xlabel('theoretical quantiles')
                    plt.ylabel('sample quantiles')
                    plt.show()
        plt.show()

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import shapiro, levene, bartlett, normaltest
import scipy.stats as stats
import warnings

warnings.filterwarnings("ignore", category=UserWarning, module="scipy")

# Separate abstract base classes for each task

class OutlierDetection:
    def detect_outliers(self, df, col):
        raise NotImplementedError

class StatisticalTest:
    def perform_test(self, df, num_col, cat_col):
        raise NotImplementedError

class AssumptionTests:
    def test_normality(self, df, num_col, cat_col):
        raise NotImplementedError

    def test_homogeneity(self, df, num_col, cat_col):
        raise NotImplementedError


# Concrete implementations

class DataOptimization:
    def __init__(self, df):
        self.df = df

    def initial_exploration(self):
        print(self.df.describe())

    def get_combinations(self, numerical_cols, categorical_cols):
        combinations = []
        for cat_col in categorical_cols:
            for num_col in numerical_cols:
                combinations.append((num_col, cat_col))
        return combinations

class OutlierDetectionIQR(OutlierDetection):
    def detect_outliers(self, df, col):
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        df['outlier_id'] = np.where((df[col] < lower_bound) | (df[col] > upper_bound), 'outlier', 'non-outlier')

        outlier_counts = df['outlier_id'].value_counts()
        total_count = len(df)
        outlier_proportions = outlier_counts / total_count

        print(f"\n{'=' * 79}")
        print(f"                    {col} Outlier Analysis")
        print(f"{'=' * 79}\n")
        print("| frequency count |")
        print("-" * 79)
        print(f"{outlier_counts}\n")
        print("| frequency distribution: |")
        print("-" * 79)
        print(f"{outlier_proportions}\n")

        return df, lower_bound, upper_bound

class NormalityTest(AssumptionTests):
    def test_normality(self, df, num_col, cat_col):
        grouped_data = df.groupby(cat_col)[num_col]
        results = {}
        for group_name, group_data in grouped_data:
            group_data = group_data.dropna()
            if len(group_data) >= 5000:
                stat, p_val = normaltest(group_data)
                results[group_name] = {"Statistic": stat, "p-value": p_val, "Normality Assumed": p_val > 0.05}
            elif len(group_data) >= 3:
                stat, p_val = shapiro(group_data)
                results[group_name] = {"Shapiro-Wilk Test Statistic": stat, "p-value": p_val, "Normality Assumed": p_val > 0.05}
            else:
                results[group_name] = "Insufficient data for normality test"
        return results

class VarianceTest(AssumptionTests):
    def test_homogeneity(self, df, num_col, cat_col):
        groups = [df[df[cat_col] == category][num_col] for category in df[cat_col].unique()]
        levene_stat, levene_p = levene(*groups)
        bartlett_stat, bartlett_p = bartlett(*groups)
        return {
            "Levene's Test": {"Statistic": levene_stat, "p-value": levene_p, "Equal Variance Assumed": levene_p > 0.05},
            "Bartlett's Test": {"Statistic": bartlett_stat, "p-value": bartlett_p, "Equal Variance Assumed": bartlett_p > 0.05}
        }

# For plotting, it is separated into a dedicated class.
class DataPlotter:
    def plot_boxplot(self, df, col, hue=None):
        sns.boxplot(x=df[col], hue=hue)
        plt.title(f"{col}")
        if hue:
            plt.legend(title='Categories', bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.show()

    def plot_ttest(self, df, num_col, cat_col):
        sns.boxplot(x=num_col, y=cat_col, data=df)
        plt.title(f"T-test: {cat_col} vs {num_col}")
        plt.show()

    def plot_anova(self, df, num_col, cat_col):
        sns.boxplot(x=num_col, y=cat_col, data=df)
        plt.title(f"ANOVA Test: {num_col} for {cat_col}")
        plt.show()


# Refactoring the main class that coordinates all tasks
class DataAnalysisPipeline:
    def __init__(self, df, outlier_detector, normality_tester, variance_tester, plotter):
        self.df = df
        self.outlier_detector = outlier_detector
        self.normality_tester = normality_tester
        self.variance_tester = variance_tester
        self.plotter = plotter

    def analyze(self, numerical_cols, categorical_cols):
        for col in numerical_cols:
            self.outlier_detector.detect_outliers(self.df, col)
            self.plotter.plot_boxplot(self.df, col, hue='outlier_id')

        combinations = DataOptimization(self.df).get_combinations(numerical_cols, categorical_cols)
        for num_col, cat_col in combinations:
            p_val = None
            if len(self.df[cat_col].unique()) == 2:
                p_val = self.perform_ttest(num_col, cat_col)
            else:
                p_val = self.perform_anova(num_col, cat_col)

            print(f"P-value for {num_col} by {cat_col}: {p_val}")

        # Test assumptions
        for num_col in numerical_cols:
            normality_results = self.normality_tester.test_normality(self.df, num_col, categorical_cols)
            variance_results = self.variance_tester.test_homogeneity(self.df, num_col, categorical_cols)

            print(f"Normality Results for {num_col}: {normality_results}")
            print(f"Variance Homogeneity Results for {num_col}: {variance_results}")

# Example of using the refactored classes
if __name__ == "__main__":
    df = pd.read_csv('data.csv')
    numerical_cols = ['col1', 'col2']
    categorical_cols = ['cat_col1', 'cat_col2']

    # Instantiate different classes
    outlier_detector = OutlierDetectionIQR()
    normality_tester = NormalityTest()
    variance_tester = VarianceTest()
    plotter = DataPlotter()

    # Create and run the analysis pipeline
    pipeline = DataAnalysisPipeline(df, outlier_detector, normality_tester, variance_tester, plotter)
    pipeline.analyze(numerical_cols, categorical_cols)

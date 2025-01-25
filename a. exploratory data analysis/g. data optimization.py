import os
import matplotlib.pyplot as plt
from scipy.stats import shapiro, levene, bartlett, normaltest
import scipy.stats as stats
import warnings

warnings.filterwarnings("ignore", category=UserWarning, module="scipy")

class DataOptimization:
    def __init__(self, df):
        self.df = df

    def initial_exploration(self):
        print(self.df.describe())

    def detect_outliers(self, col):
        Q1 = self.df[col].quantile(0.25)
        Q3 = self.df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        self.df['outlier_id'] = np.where((self.df[col] < lower_bound) | (self.df[col] > upper_bound), 'outlier', 'non-outlier')

        outlier_counts = self.df['outlier_id'].value_counts()
        total_count = len(self.df)
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

        return self.df, lower_bound, upper_bound

    def plot_outliers(self, col):
        sns.boxplot(x=self.df[col], hue=self.df['outlier_id'])
        plt.title(f"{col}")
        plt.legend(title='Categories', bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.show()

    def save_outliers(self, numerical_cols, save_dir=""):
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)

        for col in numerical_cols:
            self.df, lower, upper = self.detect_outliers(col)
            outliers_df = self.df[self.df['outlier_id'] == 'outlier']

            if not outliers_df.empty:
                filename = os.path.join(save_dir, f"{col}_outliers.csv")
                outliers_df.to_csv(filename, index=False)
                print(f"Outliers for {col} saved to {filename}")
            else:
                print(f"No outliers detected for {col}.")

    def perform_ttest(self, num_col, cat_col):
        categories = self.df[cat_col].unique()

        if len(categories) == 2:
            group1 = self.df[self.df[cat_col] == categories[0]][num_col]
            group2 = self.df[self.df[cat_col] == categories[1]][num_col]

            t_stat, p_val = stats.ttest_ind(group1, group2, nan_policy='omit')

            print(f"| T-test for {num_col} by {cat_col} |")
            print("-" * 79)
            print(f"-   T-statistic: {t_stat}")

            sns.boxplot(x=num_col, y=cat_col, data=self.df)
            plt.title(f"T-test: {categories[0]} vs {categories[1]} for {num_col}")
            plt.show()

            return p_val
        else:
            print(f"T-test not applicable for {cat_col} (needs 2 categories).")
            return None

    def perform_anova(self, num_col, cat_col):
        groups = [self.df[self.df[cat_col] == category][num_col] for category in self.df[cat_col].unique()]
        f_stat, p_val = stats.f_oneway(*groups)

        print(f"\n| ANOVA Test: {num_col} by {cat_col} |")
        print("-" * 79)
        print(f"-   F-statistic: {f_stat}")

        sns.boxplot(x=num_col, y=cat_col, data=self.df)
        plt.title(f"ANOVA Test: {num_col} for {cat_col}")
        plt.show()

        return p_val

    def get_combinations(self, numerical_cols, categorical_cols):
        combinations = []
        for cat_col in categorical_cols:
            for num_col in numerical_cols:
                combinations.append((num_col, cat_col))

        return combinations

    def test_normality_large_sample(self, data):
        stat, p_val = normaltest(data)
        return {
            "Statistic": stat,
            "p-value": p_val,
            "Normality Assumed": p_val > 0.05
        }

    def test_assumptions(self, numerical_cols, categorical_cols):
        results = {}

        for num_col in numerical_cols:
            print(f"\nTesting Column: {num_col}")
            results[num_col] = {}

            self.df[num_col] = self.df[num_col].astype("float64")

            for cat_col in categorical_cols:
                print(f"\nTesting for Categorical Column: {cat_col}")
                grouped_data = self.df.groupby(cat_col)[num_col]
                normality_results = {}
                for group_name, group_data in grouped_data:
                    group_data = group_data.dropna()
                    if len(group_data) >= 5000:
                        normality_results[group_name] = self.test_normality_large_sample(group_data)
                    elif len(group_data) >= 3:
                        stat, p_val = shapiro(group_data)
                        normality_results[group_name] = {
                            "Shapiro-Wilk Test Statistic": stat,
                            "p-value": p_val,
                            "Normality Assumed": p_val > 0.05
                        }
                    else:
                        normality_results[group_name] = "Insufficient data for normality test"

                results[num_col] = {"Normality": normality_results}
                group_values = [
                    group_data.dropna() for _, group_data in grouped_data if len(group_data.dropna()) >= 2
                ]
                if len(group_values) > 1:
                    levene_stat, levene_p = levene(*group_values)
                    bartlett_stat, bartlett_p = bartlett(*group_values)
                    results[num_col]["Homogeneity of Variance"] = {
                        "Levene's Test": {
                            "Statistic": levene_stat,
                            "p-value": levene_p,
                            "Equal Variance Assumed": levene_p > 0.05
                        },
                        "Bartlett's Test": {
                            "Statistic": bartlett_stat,
                            "p-value": bartlett_p,
                            "Equal Variance Assumed": bartlett_p > 0.05
                        }
                    }
                else:
                    results[num_col]["Homogeneity of Variance"] = "Insufficient groups for variance tests"

                print("\n" + "=" * 80)
                print(f"Results for Numerical Column: {num_col} (Categorical Column: {cat_col})")
                print("=" * 80)

                print("\nNormality Results:")
                print("-" * 80)
                for group, result in results[num_col]["Normality"].items():
                    if isinstance(result, dict):
                        print(f"Group: {group}")
                        print(f"  - Statistic: {result.get('Statistic', result.get('Shapiro-Wilk Test Statistic', 'N/A')):.4f}")
                        print(f"  - p-value: {result.get('p-value', 'N/A'):.4e}")
                        print(f"  - Normality Assumed: {'Yes' if result.get('Normality Assumed', False) else 'No'}\n")
                    else:
                        print(f"Group: {group} -> {result}\n")

                print("Homogeneity of Variance Results:")
                print("-" * 80)
                homogeneity = results[num_col].get("Homogeneity of Variance", {})
                if isinstance(homogeneity, dict):
                    for test, values in homogeneity.items():
                        print(f"{test}:")
                        print(f"  - Statistic: {values['Statistic']:.4f}")
                        print(f"  - p-value: {values['p-value']:.4e}")
                        print(f"  - Equal Variance Assumed: {'Yes' if values['Equal Variance Assumed'] else 'No'}\n")
                else:
                    print(homogeneity)

                print("=" * 80 + "\n")

        return results

if __name__ == "__main__":
    file_path = ''
    df = pd.read_csv(file_path)
    numerical_cols = ['col1', 'col2']
    categorical_cols = ['cat_col1', 'cat_col2']

    data_optimizer = DataOptimization(df)
    data_optimizer.initial_exploration()
    data_optimizer.save_outliers(numerical_cols)
    combinations = data_optimizer.get_combinations(numerical_cols, categorical_cols)

    for num_col, cat_col in combinations:
        if len(df[cat_col].unique()) == 2:
            p_val = data_optimizer.perform_ttest(num_col, cat_col)
            print(f"-   P-value: {p_val}\n")
            print("\n\n" + "-" * 88 + "\n\n")
        else:
            p_val = data_optimizer.perform_anova(num_col, cat_col)
            print("For more than 2 categories, ANOVA test is performed.")
            print(f"-   P-value: {p_val}\n")
            print("\n\n" + "-" * 88 + "\n\n")

    results = data_optimizer.test_assumptions(numerical_cols, categorical_cols)

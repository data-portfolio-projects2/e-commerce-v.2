import itertools
from scipy.stats import chi2_contingency, chisquare

class CategoricalAnalysis:
    def __init__(self, dataframe, categorical_columns):
        self.df = dataframe
        self.categorical_cols = categorical_columns

    def _generate_column_pairs(self):
        return list(itertools.combinations(self.categorical_cols, 2))

    def _print_header(self, title):
        print("\n" + "*" * 80)
        print(f"                     {title}                     ")
        print("*" * 80)

    def analyze_categorical_pairs(self):
        pairs = self._generate_column_pairs()
        for col1, col2 in pairs:
            self._print_header(f"{col1} vs. {col2}")
            contingency_table = pd.crosstab(self.df[col1], self.df[col2])
            print(f"\n| Contingency Table: |\n{contingency_table}\n")
            
            chi2, p, dof, expected = chi2_contingency(contingency_table)
            print(f"\n| Chi-Squared Test Results: |")
            print(f"Chi2: {chi2}\nP-value: {p}\nDegrees of Freedom: {dof}\n")
            
            expected_df = pd.DataFrame(expected, index=contingency_table.index, columns=contingency_table.columns)
            print(f"\n| Expected Frequencies: |\n{expected_df}\n")
            
            self._check_expected_frequencies(expected_df)
            self._perform_hypothesis_test(p)

    def _check_expected_frequencies(self, expected_df):
        if (expected_df < 5).any().any():
            print("\n| Expected Frequency Check: |")
            print("Warning: Some expected frequencies are less than 5. Chi-Square results may be unreliable.")
        else:
            print("\n| Expected Frequency Check: |")
            print("The expected frequencies are adequate for the Chi-Square test.")

    def _perform_hypothesis_test(self, p_value):
        print("\n| Hypothesis Test Result: |")
        if p_value < 0.05:
            print("Reject the Null Hypothesis: There is a significant association between the variables.")
        else:
            print("Fail to Reject the Null Hypothesis: There is no significant association between the variables.")

    def check_imbalance(self):
        results = []
        for var in self.categorical_cols:
            imbalance_info = self._check_imbalance_for_variable(var)
            results.append({'Variable': var, 'Imbalance Info': imbalance_info})
        
        self._print_imbalance_results(results)

    def _check_imbalance_for_variable(self, var):
        value_counts = self.df[var].value_counts()
        total_count = len(self.df)
        return value_counts / total_count

    def _print_imbalance_results(self, results):
        for res in results:
            print(f"\n| {res['Variable']} |")
            print(f"\n{res['Imbalance Info']}\n")
            print("Note: Check if any imbalance exceeds the threshold for assumption violations.")

    def analyze_data_distribution(self):
        for col in self.categorical_cols:
            self._print_header(f"Analysis of {col} Distribution")
            
            observed_counts = self._get_observed_counts(col)
            print(f"\n| Observed Counts: |\n{observed_counts}")
            
            expected_counts = self._get_expected_counts(observed_counts)
            print(f"\n| Expected Counts (Uniform Distribution): |\n{expected_counts}")
            
            chi2_stat, p_val, dof = self._perform_chi_square_test(observed_counts, expected_counts)
            self._print_chi_square_results(chi2_stat, p_val, dof)
            self._perform_distribution_hypothesis_test(p_val)

    def _get_observed_counts(self, col):
        return self.df[col].value_counts().sort_index()

    def _get_expected_counts(self, observed_counts):
        num_categories = len(observed_counts)
        total_count = len(self.df)
        expected_counts = np.array([total_count / num_categories] * num_categories)
        return pd.Series(expected_counts, index=observed_counts.index)

    def _perform_chi_square_test(self, observed_counts, expected_counts):
        chi2_stat, p_val = chisquare(f_obs=observed_counts, f_exp=expected_counts)
        dof = len(observed_counts) - 1
        return chi2_stat, p_val, dof

    def _print_chi_square_results(self, chi2_stat, p_val, dof):
        print(f"\n| Chi-Square Goodness of Fit Test: |")
        print(f"Chi2 Stat: {chi2_stat}")
        print(f"P-Value: {p_val}")
        print(f"Degrees of Freedom: {dof}")

    def _perform_distribution_hypothesis_test(self, p_val):
        print("\n| Hypothesis Test Result: |")
        if p_val < 0.05:
            print("The observed distribution doesn't follow the expected distribution.")
        else:
            print("The observed distribution follows the expected distribution.")

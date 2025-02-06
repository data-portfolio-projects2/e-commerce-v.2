import pandas as pd
import warnings

# Suppressing UserWarnings related to unknown format issues
warnings.filterwarnings("ignore", category=UserWarning, message=".*Could not infer format.*")

class DataCleaning:
    def __init__(self, df):
        self.df = df

    def _convert_column(self, col, dtype):
        """Helper function to convert columns to the specified data type."""
        try:
            if dtype == 'datetime':
                self.df[col] = pd.to_datetime(self.df[col], errors='coerce')
            elif dtype == 'numeric':
                self.df[col] = pd.to_numeric(self.df[col], errors='coerce')
        except Exception as e:
            print(f"Error converting column '{col}' to {dtype}: {e}")

    def clean_and_convert_dtypes(self):
        """Clean and convert data types for specific columns."""
        # Convert 'Order Date' to datetime if exists
        if 'Order Date' in self.df.columns:
            self._convert_column('Order Date', 'datetime')

        # Convert other object-type columns to datetime if applicable
        for col in self.df.select_dtypes(include=['object']).columns:
            if col != 'Order Date':  # Skip 'Order Date' since it was already handled
                self._convert_column(col, 'datetime')

        # Convert numerical columns (int64/float64) to numeric
        for col in self.df.select_dtypes(include=['int64', 'float64']).columns:
            self._convert_column(col, 'numeric')

    def clean_column_names(self):
        """Clean column names by stripping spaces, converting to lowercase, and replacing spaces with underscores."""
        self.df.columns = self.df.columns.str.strip().str.lower().str.replace(' ', '_')

    def clean_values(self):
        """Clean values in object columns by stripping leading/trailing spaces."""
        for col in self.df.select_dtypes(include=['object']).columns:
            self.df[col] = self.df[col].str.strip()

    def validate_column_names(self):
        """Validate that column names don't have leading/trailing spaces."""
        spaces_in_columns = [col for col in self.df.columns if col != col.strip()]
        if spaces_in_columns:
            print(f" Warning: [ Some column names still have leading/trailing spaces: {spaces_in_columns} ]\n")
        else:
            print("Result: [ All column names are clean with no leading/trailing spaces.]\n")
        return spaces_in_columns

    def perform_data_cleaning(self):
        """Perform a complete data cleaning process."""
        self.clean_column_names()
        self.clean_and_convert_dtypes()
        self.clean_values()

    def display_data_info(self):
        """Display information on data cleaning results."""
        print("\n| 1. Data types after conversion: |")
        print(f"{self.df.dtypes}\n")
        print("\n| 2. Leading/trailing spaces validation: |")
        self.validate_column_names()
        print("\n| 3. Data columns after conversion: |")
        print(f"{self.df.columns}\n")
        print("\n| 4. Data after conversion: |")
        print(self.df.head())

# Example usage:
# df = pd.read_csv("your_file.csv")
# data_cleaning = DataCleaning(df)
# data_cleaning.perform_data_cleaning()
# data_cleaning.display_data_info()

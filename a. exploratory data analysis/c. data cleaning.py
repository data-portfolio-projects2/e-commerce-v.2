import warnings

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
            logging.info(f"Successfully converted column '{col}' to {dtype}.")
        except Exception as e:
            logging.error(f"Error converting column '{col}' to {dtype}: {e}")

    def clean_and_convert_dtypes(self):
        """Clean and convert data types for specific columns."""
        try:
            if 'Order Date' in self.df.columns:
                self._convert_column('Order Date', 'datetime')
            
            for col in self.df.select_dtypes(include=['object']).columns:
                if col != 'Order Date':
                    self._convert_column(col, 'datetime')
            
            for col in self.df.select_dtypes(include=['int64', 'float64']).columns:
                self._convert_column(col, 'numeric')
        except Exception as e:
            logging.error(f"Error in clean_and_convert_dtypes: {e}")

    def clean_column_names(self):
        """Clean column names by stripping spaces, converting to lowercase, and replacing spaces with underscores."""
        try:
            self.df.columns = self.df.columns.str.strip().str.lower().str.replace(' ', '_')
            logging.info("Column names cleaned successfully.")
        except Exception as e:
            logging.error(f"Error cleaning column names: {e}")

    def clean_values(self):
        """Clean values in object columns by stripping leading/trailing spaces."""
        try:
            for col in self.df.select_dtypes(include=['object']).columns:
                self.df[col] = self.df[col].str.strip()
            logging.info("Object column values cleaned successfully.")
        except Exception as e:
            logging.error(f"Error cleaning values: {e}")

    def validate_column_names(self):
        """Validate that column names don't have leading/trailing spaces."""
        try:
            spaces_in_columns = [col for col in self.df.columns if col != col.strip()]
            if spaces_in_columns:
                logging.warning(f"Some column names still have leading/trailing spaces: {spaces_in_columns}")
            else:
                logging.info("All column names are clean with no leading/trailing spaces.")
            return spaces_in_columns
        except Exception as e:
            logging.error(f"Error validating column names: {e}")
            return []

    def perform_data_cleaning(self):
        """Perform a complete data cleaning process."""
        try:
            self.clean_column_names()
            self.clean_and_convert_dtypes()
            self.clean_values()
            logging.info("Data cleaning completed successfully.")
        except Exception as e:
            logging.error(f"Error in perform_data_cleaning: {e}")

    def display_data_info(self):
        """Display information on data cleaning results."""
        try:
            logging.info("Displaying data information after cleaning.")
            print("\n| 1. Data types after conversion: |")
            print(f"{self.df.dtypes}\n")
            print("\n| 2. Leading/trailing spaces validation: |")
            self.validate_column_names()
            print("\n| 3. Data columns after conversion: |")
            print(f"{self.df.columns}\n")
            print("\n| 4. Data after conversion: |")
            print(self.df.head())
        except Exception as e:
            logging.error(f"Error displaying data information: {e}")

# Example usage:
# df = pd.read_csv("your_file.csv")
# data_cleaning = DataCleaning(df)
# data_cleaning.perform_data_cleaning()
# data_cleaning.display_data_info()

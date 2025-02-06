class DataIntegrity:
    def __init__(self, df):
        self.df = df

    def _check_and_save(self, check_type, condition, file_name, description):
        """Helper method for checking conditions and saving results"""
        try:
            rows = self.df[condition]
            if not rows.empty:
                logging.info(f"| Checking for {check_type} | Result: [ {description} Saving rows to {file_name}. ]")
                rows.to_csv(file_name, index=False)
            else:
                logging.info(f"| Checking for {check_type} | Result: [ No {description} found. ]")
        except Exception as e:
            logging.error(f"Error while checking {check_type}: {e}")

    def handle_missing_values(self, missing_value_rows_file):
        self._check_and_save(
            check_type="missing values", 
            condition=self.df.isnull().any(axis=1),
            file_name=missing_value_rows_file,
            description="Missing values"
        )

    def handle_order_id_duplicates(self, duplicate_order_id_file):
        self._check_and_save(
            check_type="duplicated 'Order ID'",
            condition=self.df.duplicated(subset=['Order ID'], keep=False),
            file_name=duplicate_order_id_file,
            description="duplicate 'Order ID'"
        )

    def print_column_summary(self):
        """Print summary of column integrity checks (duplicates and missing values)"""
        try:
            logging.info("| Column Summary (duplicates in 'Order ID' | missing values count): |")
            column_summary = pd.DataFrame(columns=["columns", "duplicates (Order ID)", "missing values (count)"])
            for col in self.df.columns:
                duplicates_count = self.df.duplicated(subset=['Order ID'], keep=False).sum() if col == 'Order ID' else 0
                missing_count = self.df[col].isnull().sum()
                column_summary.loc[len(column_summary)] = [col, duplicates_count, missing_count]
            logging.info(f"\n{column_summary}")
        except Exception as e:
            logging.error(f"Error while generating column summary: {e}")

    def perform_data_integrity_checks(self, missing_value_rows_file, duplicate_order_id_file):
        """Performs the full set of data integrity checks"""
        try:
            self.handle_missing_values(missing_value_rows_file)
            self.handle_order_id_duplicates(duplicate_order_id_file)
            self.print_column_summary()
        except Exception as e:
            logging.error(f"Error during data integrity checks: {e}")

# Example usage:
# df = pd.read_csv("your_file.csv")
# data_integrity = DataIntegrity(df)
# data_integrity.perform_data_integrity_checks("missing_rows.csv", "duplicate_orders.csv")

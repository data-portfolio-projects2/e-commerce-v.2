class DataIntegrity:
    def __init__(self, df):
        self.df = df

    def handle_missing_values(self, missing_value_rows_file):
        missing_rows = self.df[self.df.isnull().any(axis=1)]
        if not missing_rows.empty:
            print("| Checking for missing values |")
            print(f"Result: [ Missing values found. Saving rows with missing values to {missing_value_rows_file}. ]\n")
            missing_rows.to_csv(missing_value_rows_file, index=False)
        else:
            print("| Checking for missing values |")
            print("Result: [ No missing values found. ]\n")

    def handle_order_id_duplicates(self, duplicate_order_id_file):
        duplicate_rows = self.df[self.df.duplicated(subset=['Order ID'], keep=False)]
        if not duplicate_rows.empty:
            print("| Checking for duplicated values |")
            print(f"Result: [ Found {len(duplicate_rows)} rows with duplicate 'Order ID's. Saving them to {duplicate_order_id_file}. ]\n")
            duplicate_rows.to_csv(duplicate_order_id_file, index=False)
        else:
            print("| Checking for duplicated values |")
            print("Result: [ No duplicate 'Order ID's found. ]\n")

    def print_column_summary(self):
        print("| Column Summary (duplicates in 'Order ID' | missing values count): |")
        column_summary = pd.DataFrame(columns=["columns", "duplicates (Order ID)", "missing values (count)"])
        for col in self.df.columns:
            duplicates_count = self.df.duplicated(subset=['Order ID'], keep=False).sum() if col == 'Order ID' else 0
            missing_count = self.df[col].isnull().sum()
            new_row = pd.DataFrame({
                "columns": [col],
                "duplicates (Order ID)": [duplicates_count],
                "missing values (count)": [missing_count]
            })
            column_summary = pd.concat([column_summary, new_row], ignore_index=True)
        print(column_summary)

    def perform_data_integrity_checks(self, missing_value_rows_file, duplicate_order_id_file):
        self.handle_missing_values(missing_value_rows_file)
        self.handle_order_id_duplicates(duplicate_order_id_file)
        self.print_column_summary()

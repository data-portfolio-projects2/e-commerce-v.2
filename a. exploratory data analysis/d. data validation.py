class DataValidation:
    def __init__(self, df):
        self.df = df

    def validate_column(self, column, valid_values=None, value_range=None, dtype=None, custom_format=None):
        """
        Generalized column validation method to check different conditions.
        """
        # Check for column existence
        if column not in self.df.columns:
            print(f"Warning: '{column}' does not exist in the DataFrame.")
            return

        # Check for correct data type
        if dtype:
            if not pd.api.types.is_dtype_equal(self.df[column].dtype, dtype):
                print(f"Warning: '{column}' is not of type {dtype}.")
        
        # Validate against a range
        if value_range:
            if not self.df[column].between(value_range[0], value_range[1]).all():
                print(f"Warning: '{column}' contains values outside the expected range.")
        
        # Validate against a list of valid values
        if valid_values is not None:
            invalid_values = self.df[column][~self.df[column].isin(valid_values)]
            if not invalid_values.empty:
                print(f"Warning: Invalid values found in '{column}':\n{invalid_values}")
            else:
                print(f"Result: All values in '{column}' are valid.")
        
        # Apply custom format validation
        if custom_format:
            valid_format = self.df[column].apply(custom_format).notna()
            if not valid_format.all():
                print(f"Warning: Some values in '{column}' do not match the expected format.")

    def order_id_validation(self):
        self.validate_column('order_id', value_range=(100000, 999999))

    def order_date_validation(self):
        self.validate_column('order_date', custom_format=lambda x: pd.to_datetime(x, errors='coerce'))

    def product_id_validation(self):
        valid_product_ids = ['BF1543', 'BF1544', 'BF1545', 'BF1546', 'BF1547', 'BF1548', 'BF1549', 'BF1550', 'BF1551', 'BF1552', 'BF1553', 'BF1554', 'BF1555']
        self.validate_column('product_id', valid_values=valid_product_ids)

    def product_category_validation(self):
        valid_categories = ['Clothing', 'Other', 'Ornaments']
        self.validate_column('product_category', valid_values=valid_categories)

    def buyer_gender_validation(self):
        valid_genders = ['Male', 'Female']
        self.validate_column('buyer_gender', valid_values=valid_genders)

    def validate_buyer_age(self):
        self.validate_column('buyer_age', dtype='int64', value_range=(18, None))

    def order_location_validation(self):
        valid_locations = ['New Jersey', 'Las Vegas', 'Cardiff', 'Pittsburgh', 'Miami', 'Sydney', 'Memphis', 'New York', 'Montreal', 'Sacramento', 'Paris', 'San Antonio', 'Cleveland', 'London', 'Portland', 'Detroit', 'Dublin', 'Glasgow', 'Austin', 'Toronto', 'Mumbai', 'San Francisco', 'Manchester', 'Liverpool', 'New Delhi']
        self.validate_column('order_location', valid_values=valid_locations)

    def international_shipping_validation(self):
        valid_shipping_options = ['No', 'Yes']
        self.validate_column('international_shipping', valid_values=valid_shipping_options)

    def sales_price_validation(self):
        valid_sales_prices = [100, 9, 10, 118, 32, 65, 130, 97, 15, 45, 50, 20, 23]
        self.validate_column('sales_price', valid_values=valid_sales_prices)

    def shipping_charges_validation(self):
        valid_shipping_charges = [0, 40, 100, 25, 50, 70]
        self.validate_column('shipping_charges', valid_values=valid_shipping_charges)

    def sales_per_unit_validation(self):
        self.validate_column('sales_per_unit', dtype='float64')

    def quantity_validation(self):
        self.validate_column('quantity', dtype='int64')

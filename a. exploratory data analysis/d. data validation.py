class DataValidation:
    def __init__(self, df):
        self.df = df

    def order_id_validation(self):
        valid_order_ids = self.df['order_id'].between(100000, 999999)
        invalid_ids_df = self.df[~valid_order_ids].loc[:, 'order_id'].to_frame(name='Order ID')

        if not invalid_ids_df.empty:
            print("-    Warning: invalid order_id format\n")
            print(invalid_ids_df)
        else:
            print("-    Result: All values are in standard order_id format\n")

    def order_date_validation(self):
        valid_dates = pd.to_datetime(self.df['order_date'], errors='coerce', format='%Y-%m-%d')
        invalid_dates_df = self.df[valid_dates.isna()].loc[:, 'order_date'].to_frame(name='Order Date')

        if not invalid_dates_df.empty:
            print("-    Warning: invalid order_date format\n")
            print(invalid_dates_df)
        else:
            print("-    Result: All values are in standard ISO 8601 format\n")

    def product_id_validation(self):
        valid_product_ids = ['BF1543', 'BF1544', 'BF1545', 'BF1546', 'BF1547', 'BF1548', 
                              'BF1549', 'BF1550', 'BF1551', 'BF1552', 'BF1553', 'BF1554', 
                              'BF1555']
        invalid_product_ids = self.df['product_id'][~self.df['product_id'].isin(valid_product_ids)]

        if not invalid_product_ids.empty:
            print("-    Warning: invalid product id/s:\n")
            print(invalid_product_ids)
        else:
            print("-    Result: All product id's are valid\n")

    def product_category_validation(self):
        valid_product_categories = ['Clothing', 'Other', 'Ornaments']
        invalid_categories = self.df['product_category'][~self.df['product_category'].isin(valid_product_categories)]

        if not invalid_categories.empty:
            print("-    Warning: invalid product category/s:\n")
            print(invalid_categories)
        else:
            print("-    Result: All product categories are valid.\n")

    def buyer_gender_validation(self):
        valid_buyer_genders = ['Male', 'Female']
        invalid_genders = self.df['buyer_gender'][~self.df['buyer_gender'].isin(valid_buyer_genders)]

        if not invalid_genders.empty:
            print("-    Warning: invalid buyer gender/s:\n")
            print(invalid_genders)
        else:
            print("-    Result: All buyer gender category/s are valid.\n")

    def validate_buyer_age(self):
        if not pd.api.types.is_numeric_dtype(self.df['buyer_age']):
            print("-    Result: Warning: some value/s is/are not numeric.\n")

        if pd.api.types.is_integer_dtype(self.df['buyer_age']):
            print(f"-   Result: value/s is/are of integer type: {self.df['buyer_age'].dtype}.\n")

            if (self.df['buyer_age'] < 18).any():
                print("-    Warning: 'buyer_age' value/s is/are under age (18).\n")
        else:
            print("-    Warning: 'buyer_age' value/s is/are not of integer type.\n")

    def order_location_validation(self):
        valid_order_locations = [
            'New Jersey', 'Las Vegas', 'Cardiff', 'Pittsburgh', 'Miami', 'Sydney',
            'Memphis', 'New York', 'Montreal', 'Sacramento', 'Paris', 'San Antonio',
            'Cleveland', 'London', 'Portland', 'Detroit', 'Dublin', 'Glasgow', 'Austin',
            'Toronto', 'Mumbai', 'San Francisco', 'Manchester', 'Liverpool', 'New Delhi'
        ]
        invalid_locations = self.df['order_location'][~self.df['order_location'].isin(valid_order_locations)]

        if not invalid_locations.empty:
            print("-    Warning: invalid order location/s:\n")
            print(invalid_locations)
        else:
            print("-    Result: All order locations are valid.\n")

    def international_shipping_validation(self):
        valid_shipping_options = ['No', 'Yes']
        invalid_shipping = self.df['international_shipping'][~self.df['international_shipping'].isin(valid_shipping_options)]

        if not invalid_shipping.empty:
            print("-    Warning: invalid international_shipping value/s found:\n")
            print(invalid_shipping)
        else:
            print("-    Result: All 'international_shipping' values are valid.\n")

    def sales_price_validation(self):
        valid_sales_prices = [100, 9, 10, 118, 32, 65, 130, 97, 15, 45, 50, 20, 23]
        
        if not pd.api.types.is_numeric_dtype(self.df['sales_price']):
            print("-    Warning: 'sales_price' values are not numeric.\n")
        else:
            print("-    Result: 'sales_price' values are numeric.\n")

        invalid_sales_prices = self.df['sales_price'][~self.df['sales_price'].isin(valid_sales_prices)]

        if not invalid_sales_prices.empty:
            print("-    Warning: 'sales_price' contains invalid values:\n")
            print(invalid_sales_prices)
        else:
            print("-    Result: All 'sales_price' values are valid.\n")

        negative_sales_prices = self.df['sales_price'][self.df['sales_price'] < 0]

        if not negative_sales_prices.empty:
            print("-    Warning: 'sales_price' contains negative values:\n")
            print(negative_sales_prices)
        else:
            print("-    Result: All 'sales_price' values are positive.\n")

    def shipping_charges_validation(self):
        valid_shipping_charges = [0, 40, 100, 25, 50, 70]

        if not pd.api.types.is_numeric_dtype(self.df['shipping_charges']):
            print("-    Warning: 'shipping_charges' values are not numeric.\n")
        else:
            print("-    Result: 'shipping_charges' values are numeric.\n")

        invalid_shipping_charges = self.df['shipping_charges'][~self.df['shipping_charges'].isin(valid_shipping_charges)]

        if not invalid_shipping_charges.empty:
            print("-    Warning: 'shipping_charges' contains invalid values:\n")
            print(invalid_shipping_charges)
        else:
            print("-    Result: All 'shipping_charges' values are valid.\n")

        negative_shipping_charges = self.df['shipping_charges'][self.df['shipping_charges'] < 0]

        if not negative_shipping_charges.empty:
            print("-    Warning: 'shipping_charges' contains negative values:\n")
            print(negative_shipping_charges)
        else:
            print("-    Result: All 'shipping_charges' values are positive.\n")

    def sales_per_unit_validation(self):
        if not pd.api.types.is_numeric_dtype(self.df['sales_per_unit']):
            print("-    Warning: 'sales_per_unit' values are not numeric.\n")
        else:
            print("-    Result: 'sales_per_unit' values are numeric.\n")

        negative_sales_per_unit = self.df['sales_per_unit'][self.df['sales_per_unit'] < 0]

        if not negative_sales_per_unit.empty:
            print("-    Warning: 'sales_per_unit' contains negative values:\n")
            print(negative_sales_per_unit)
        else:
            print("-    Result: All 'sales_per_unit' values are positive.\n")

    def quantity_validation(self):
        if not pd.api.types.is_numeric_dtype(self.df['quantity']):
            print("-    Warning: 'quantity' values are not numeric.\n")
        else:
            print("-    Result: 'quantity' values are numeric.\n")

        negative_quantity = self.df['quantity'][self.df['quantity'] < 0]

        if not negative_quantity.empty:
            print("-    Warning: 'quantity' contains negative values:\n")
            print(negative_quantity)
        else:
            print("-    Result: All 'quantity' values are positive.\n")

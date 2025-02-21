    @time
    @memory
    def transform():
        df = transform.extract_data()
        df = transform.order_id(df)
        df = transform.delete_col(df)
        df = transform.remove_space(df)
        df = transform.lowercase_col(df)
        df = transform.strip_space(df)
        df = transform.replace_(df)
        transform.save_df(df)
        transform.sales_data(df)
        validate.validate_product()
        validate.validate_sku()
        validate.validate_order_status()
        validate.validate_shipping()
        validate.validate_payment()
        validate.validate_gender()
        validate.validate_membership()
        validate.validate_addontotal()
        validate.validate_age()
        validate.validate_id()
        validate.validate_date()
        validate.validate_rating()
        validate.validate_totalprice()
        validate.validate_unitprice()

   

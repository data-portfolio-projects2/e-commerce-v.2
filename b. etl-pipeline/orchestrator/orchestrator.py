class Run(metaclass=static):

    @time
    @memory
    def download():
        download.authenticate_kaggle()
        download.initiate_os()
        download.download_data()

    @time
    @memory
    def transform():
        df = transform.extract_data()
        df = transform.delete_col(df)
        df = transform.remove_space(df)
        df = transform.lowercase_col(df)
        df = transform.strip_space(df)
        df = transform.replace_(df)
        df = transform.save_col(df)

    @time
    @memory
    def validate():
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

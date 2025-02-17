class Downloader(metaclass=static):

    def authenticate_kaggle():
        load.authenticate_kaggle()

    def initiate_os():
        load.initiate_os()
    
    def download_data():
        load.download_data()


class Transformer(metaclass=static):

    def extract_data():
        df = extract.extract_data()
        return df
    
    def delete_col(df):
        df = transform.delete_col(df)
        return df
    
    def remove_space(df):
        df = transform.remove_space(df)
        return df
    
    def lowercase_col(df):
        df = transform.lowercase_col(df)
        return df
    
    def strip_space(df):
        df = transform.strip_space(df)
        return df
    
    def replace_(df):
        df = transform.replace_(df)
        return df 
    
    def save_col(df):
        df = save.save_col(df)
        return df


class Validator(metaclass=static):
             
    def validate_product():
        return validate.validate_product()

    def validate_sku():
        return validate.validate_sku()

    def validate_order_status():
        return validate.validate_order_status()

    def validate_shipping():
        return validate.validate_shipping()

    def validate_payment():
        return validate.validate_payment()

    def validate_gender():
        return validate.validate_gender()

    def validate_membership():
        return validate.validate_membership()

    def validate_addontotal():
        return validate.validate_addontotal()

    def validate_age():
        return validate.validate_age()

    def validate_id():
        return validate.validate_id()

    def validate_date():
        return validate.validate_date()

    def validate_rating():
        return validate.validate_rating()

    def validate_totalprice():
        return validate.validate_totalprice()

    def validate_unitprice():
        return validate.validate_unitprice()
    




class Extractor(metaclass=static):

    def extract_data():
        df = extract.extract_data()
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
        df = extract.save_col(df)
        return df

    @time
    @memory
    def __call__(self):
        df = self.extract_data()
        df = self.lowercase_col(df)
        df = self.strip_space(df)
        df = self.replace_(df)
        df = self.save_col(df)
        


class Transform(metaclass=static): 
    
    def df_extract(file_path):
        df = transform.extract_df(file_path)
        df = df.drop(['Add-ons Purchased'], axis=1)
        return df
    
    def to_string(df):
        df = transform.to_string(df)
        return df
    
    def col_lowercase(df):
        df = transform.lowercase_col(df)
        return df
    
    def col_remove_space(df):
        df = transform.strip_space(df)
        return df
    
    def col_replace_(df):
        df = transform.replace_(df)
        return df
    
    def savedf(df):
        df.to_csv(path.df, index=False)
        return df
    
    def __call__(self):
        df = self.df_extract(path.csv)
        df = df.compute()
        #df = self.to_string(df)
        df = self.col_lowercase(df)
        df = self.col_remove_space(df)
        df = self.col_replace_(df)
        df = self.savedf(df)




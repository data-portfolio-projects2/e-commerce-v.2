from extract import DataDownloader, CSVExtractor, DataAnalyzer, DataSaver
from transform import DataTransformer
from credentials import path
from monitor import Static


class Extract(metaclass=Static):

    def download():
        download = DataDownloader()
        download()

    def extract():
        df = CSVExtractor.extract_csv()
        return df
        
    def savedf(df):
        df.to_csv(path.df, index=False)
        return df

    def analyze(df):
        DataAnalyzer.preview_data(df)
        df = DataAnalyzer.check_missing(df)
        return df

    def save(df):
        return DataSaver.save_missing(df)

    def __call__(self):
        self.download()
        df = self.extract()
        df = df.compute()
        df = self.savedf(df)
        df = self.analyze(df)
        self.save(df)


class Transform(metaclass=Static): 
    
    def df_extract(file_path):
        df = DataTransformer.extract_df(file_path)
        df = df.drop(['Add-ons Purchased'], axis=1)
        return df
    
    def to_string(df):
        df = DataTransformer.to_string(df)
        return df
    
    def col_lowercase(df):
        df = DataTransformer.lowercase_col(df)
        return df
    
    def col_remove_space(df):
        df = DataTransformer.strip_space(df)
        return df
    
    def col_replace_(df):
        df = DataTransformer.replace_(df)
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


        



        


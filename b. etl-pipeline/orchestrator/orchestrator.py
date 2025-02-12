# Import extract
from extract import DataDownloader
from extract import CSVExtractor
from extract import DataAnalyzer
from extract import DataSaver
from transform import DataTransformer
from credentials import path

class Extract:

    def download(self):
        downloader = DataDownloader()
        downloader()
    
    def extract(self, file_path):
        extractor = CSVExtractor(file_path)
        df = extractor.extract_csv()
        return df

    def savedf(self, df):
        df.to_csv(path.df, index=False)
        return df

    def analyze(self, df):
        analyzer = DataAnalyzer(df)
        analyzer.preview_data()
        missing_rows = analyzer.check_missing()
        return missing_rows

    def save(self, data):
        saver = DataSaver(data)
        saver.save_missing()

    def __call__(self):
        self.download()
        df = self.extract(path.csv)
        df = df.compute()
        df = self.savedf(df)
        df = self.analyze(df)
        self.save(df)


class Transform: 
    
    def df_extract(self, file_path):
        dt = DataTransformer()
        extr = dt.extract_df(file_path)
        extr = extr.drop(['Add-ons Purchased'], axis=1)
        return extr
    
    def col_lowercase(self, df):
        dt = DataTransformer()
        lower = dt.lowercase_col(df)
        return lower
    
    def col_remove_space(self, df):
        dt = DataTransformer()
        strip = dt.strip_space(df)
        return strip
    
    def col_replace_(self, df):
        dt = DataTransformer()
        replace_ = dt.replace_(df)
        return replace_
    
    def __call__(self):
        df = self.df_extract(path.df)
        df = df.compute()
        df = self.col_lowercase(df)
        df = self.col_remove_space(df)
        df = self.col_replace_(df)


        

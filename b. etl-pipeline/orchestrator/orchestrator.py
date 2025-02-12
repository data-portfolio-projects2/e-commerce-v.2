# Import extract
from extract import DataDownloader
from extract import CSVExtractor
from extract import DataAnalyzer
from extract import DataSaver
from credentials import path

class Extract:

    def download(self):
        downloader = DataDownloader()
        downloader()
    
    def extract(self):
        extractor = CSVExtractor(path.csv)
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

    def save(self, missing_rows):
        saver = DataSaver(missing_rows)
        saver() 

    def __call__(self):
        self.download()
        df = self.extract()
        df = df.compute()
        df = self.savedf(df)
        df = self.analyze(df)
        self.save(df)

#class Transform: 
    
#    def call_load(self):
#        pass


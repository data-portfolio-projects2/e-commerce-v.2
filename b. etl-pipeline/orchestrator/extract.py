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

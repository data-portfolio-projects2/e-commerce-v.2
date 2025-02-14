
class Extract(metaclass=static):

    def download():
        download = load()
        download()

    def extract():
        df = csv.extract_csv()
        return df
        
    def savedf(df):
        df.to_csv(path.df, index=False)
        return df

    def analyze(df):
        analyze.preview_data(df)
        df = analyze.check_missing(df)
        return df

    def save(df):
        return save.save_missing(df)

    def __call__(self):
        self.download()
        df = self.extract()
        df = df.compute()
        df = self.savedf(df)
        df = self.analyze(df)
        self.save(df)
        

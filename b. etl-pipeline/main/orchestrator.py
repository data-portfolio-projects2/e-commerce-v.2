# Import extract
from credentials import load
from credentials import path
from extract import DataDownloader
from extract import CSVExtractor
from extract import DataAnalyzer
from extract import DataSaver

class Extract:

    def call_extract(self):
        downloader = DataDownloader()
        downloader()

        extractor = CSVExtractor()
        df = extractor.extract_csv(path.csv)

        analyzer = DataAnalyzer(df)
        analyzer.preview_data()
        missing_rows = analyzer.check_missing()

        saver = DataSaver(missing_rows)
        saver()

if __name__ == "__main__":
    extract = Extract()
    extract.call_extract()



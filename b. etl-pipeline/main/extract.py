if __name__ == "__main__":

from extract import DataDownloader
from extract import CSVExtractor
from extract import DataAnalyzer
from extract import DataSaver

downloader = DataDownloader("data")
downloader()

extract = CSVExtractor("data")
df = extract.extract_csv(file_path)

analyze = DataAnalyzer(df)
analyze.preview_data()
missing_rows = analyze.check_missing()

saver = DataSaver(missing_rows)
saver.save_missing()

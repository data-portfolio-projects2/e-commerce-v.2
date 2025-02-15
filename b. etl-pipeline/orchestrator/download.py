class Downloader(metaclass=static):

    def authenticate_kaggle():
        load.authenticate_kaggle()

    def initiate_os():
        load.initiate_os()
    
    def download_data():
        load.download_data()

    def __call__(self):
        self.authenticate_kaggle()
        self.initiate_os()
        self.download_data()

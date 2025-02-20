class Run(metaclass=static):

    @time
    @memory
    def extract():
        download.authenticate_kaggle()
        download.initiate_os()
        download.download_data()


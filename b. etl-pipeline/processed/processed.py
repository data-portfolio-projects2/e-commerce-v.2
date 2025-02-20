class processed(metaclass=static):

    def data():
        return dd.read_csv("data.csv")
    
    def sales():
        return dd.read_csv("sales.csv", dtype=str) # , usecols=lambda col: col != "Unnamed: 0"

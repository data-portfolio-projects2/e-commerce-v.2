import pandas as pd
import numpy as np

class DataOptimizer:
    def __init__(self, df):
        self.df = df

    def optimize_memory_usage(self):
        start_mem = self.df.memory_usage().sum() / 1024**2
        for col in self.df.columns:
            col_type = self.df[col].dtype
            if col_type != object:
                c_min, c_max = self._get_min_max(col)
                self._downcast_column(col, c_min, c_max, col_type)
        end_mem = self.df.memory_usage().sum() / 1024**2
        print(f'Memory usage reduced to {end_mem:5.2f} MB ({100 * end_mem / start_mem:.1f}% of the initial size)')
        return self.df

    def _get_min_max(self, col):
        """ Helper function to get min and max values of a column """
        return self.df[col].min(), self.df[col].max()

    def _downcast_column(self, col, c_min, c_max, col_type):
        """ Downcast column based on type (int or float) """
        if str(col_type)[:3] == 'int':
            self._downcast_int(col, c_min, c_max)
        else:
            self._downcast_float(col, c_min, c_max)

    def _downcast_int(self, col, c_min, c_max):
        """ Downcast integer column to the most appropriate type """
        if c_min > np.iinfo(np.int8).min and c_max < np.iinfo(np.int8).max:
            self.df[col] = self.df[col].astype(np.int8)
        elif c_min > np.iinfo(np.int16).min and c_max < np.iinfo(np.int16).max:
            self.df[col] = self.df[col].astype(np.int16)
        elif c_min > np.iinfo(np.int32).min and c_max < np.iinfo(np.int32).max:
            self.df[col] = self.df[col].astype(np.int32)
        else:
            self.df[col] = self.df[col].astype(np.int64)

    def _downcast_float(self, col, c_min, c_max):
        """ Downcast float column to the most appropriate type """
        if c_min > np.finfo(np.float16).min and c_max < np.finfo(np.float16).max:
            self.df[col] = self.df[col].astype(np.float16)
        elif c_min > np.finfo(np.float32).min and c_max < np.finfo(np.float32).max:
            self.df[col] = self.df[col].astype(np.float32)
        else:
            self.df[col] = self.df[col].astype(np.float64)

    def initial_exploration(self):
        """ Initial exploration of the dataset """
        print("\n1. Optimizing memory usage...\n")
        self.df = self.optimize_memory_usage()
        print("\n2. Initial exploration...\n")
        print(self.df.info())
        print("\n3. Columns\n")
        print(self.df.columns)
        print("\n4. Initial data...\n")
        print(self.df.head())

# Example usage
# df = pd.read_csv("your_file.csv")
# optimizer = DataOptimizer(df)
# optimizer.initial_exploration()


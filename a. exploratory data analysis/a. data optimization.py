import pandas as pd
import numpy as np

class DataOptimization:
    def __init__(self, df):
        self.df = df

    def optimize_memory_usage(self):
        start_mem = self.df.memory_usage().sum() / 1024**2
        for col in self.df.columns:
            col_type = self.df[col].dtype
            if col_type != object:
                c_min = self.df[col].min()
                c_max = self.df[col].max()
                if str(col_type)[:3] == 'int':
                    self._downcast_int(col, c_min, c_max)
                else:
                    self._downcast_float(col, c_min, c_max)
        end_mem = self.df.memory_usage().sum() / 1024**2
        print(f'Memory usage reduced to {end_mem:5.2f} MB ({100 * end_mem / start_mem:.1f}% of the initial size)')
        return self.df

    def _downcast_int(self, col, c_min, c_max):
        if c_min > np.iinfo(np.int8).min and c_max < np.iinfo(np.int8).max:
            self.df[col] = self.df[col].astype(np.int8)
        elif c_min > np.iinfo(np.int16).min and c_max < np.iinfo(np.int16).max:
            self.df[col] = self.df[col].astype(np.int16)
        elif c_min > np.iinfo(np.int32).min and c_max < np.iinfo(np.int32).max:
            self.df[col] = self.df[col].astype(np.int32)
        elif c_min > np.iinfo(np.int64).min and c_max < np.iinfo(np.int64).max:
            self.df[col] = self.df[col].astype(np.int64)

    def _downcast_float(self, col, c_min, c_max):
        if c_min > np.finfo(np.float16).min and c_max < np.finfo(np.float16).max:
            self.df[col] = self.df[col].astype(np.float16)
        elif c_min > np.finfo(np.float32).min and c_max < np.finfo(np.float32).max:
            self.df[col] = self.df[col].astype(np.float32)
        else:
            self.df[col] = self.df[col].astype(np.float64)

    def initial_exploration(self):
        print("\n1. Optimizing memory usage...\n")
        self.df = self.optimize_memory_usage()
        print("\n2. Initial exploration...\n")
        print(self.df.info())
        print("\n3. Columns\n")
        print(self.df.columns)
        print("\n4. Initial data...\n")
        print(self.df.head())

# Usage
file_path = ''
df = pd.read_csv(file_path)

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

data_optimizer = DataOptimization(df)
data_optimizer.initial_exploration()

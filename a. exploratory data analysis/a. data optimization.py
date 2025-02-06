import pandas as pd
import numpy as np
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DataOptimizer:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def optimize_memory_usage(self) -> pd.DataFrame:
        """Optimizes memory usage by downcasting numeric columns."""
        try:
            start_mem = self.df.memory_usage().sum() / 1024**2
            for col in self.df.select_dtypes(include=[np.number]).columns:
                self._downcast_column(col)
            end_mem = self.df.memory_usage().sum() / 1024**2
            reduction_percent = 100 * end_mem / start_mem
            logging.info(f'Memory usage reduced to {end_mem:.2f} MB ({reduction_percent:.1f}% of the initial size)')
            return self.df
        except Exception as e:
            logging.error(f"Error optimizing memory usage: {e}")
            return self.df

    def _downcast_column(self, col: str):
        """ Downcast numeric columns based on their type."""
        try:
            col_type = self.df[col].dtype
            c_min, c_max = self.df[col].min(), self.df[col].max()

            if np.issubdtype(col_type, np.integer):
                self.df[col] = self._downcast_int(col, c_min, c_max)
            elif np.issubdtype(col_type, np.floating):
                self.df[col] = self._downcast_float(col, c_min, c_max)
        except Exception as e:
            logging.error(f"Error downcasting column {col}: {e}")

    def _downcast_int(self, col: str, c_min: int, c_max: int) -> pd.Series:
        """Downcast integer column to the most appropriate type."""
        int_types = [np.int8, np.int16, np.int32, np.int64]
        for dtype in int_types:
            if np.iinfo(dtype).min <= c_min <= c_max <= np.iinfo(dtype).max:
                return self.df[col].astype(dtype)
        return self.df[col]

    def _downcast_float(self, col: str, c_min: float, c_max: float) -> pd.Series:
        """Downcast float column to the most appropriate type."""
        float_types = [np.float16, np.float32, np.float64]
        for dtype in float_types:
            if np.finfo(dtype).min <= c_min <= c_max <= np.finfo(dtype).max:
                return self.df[col].astype(dtype)
        return self.df[col]

    def initial_exploration(self):
        """Performs initial exploration of the dataset."""
        try:
            logging.info("Starting initial data exploration...")
            self.df = self.optimize_memory_usage()
            logging.info("Dataset Info:")
            logging.info(self.df.info())
            logging.info("Columns:")
            logging.info(self.df.columns.tolist())
            logging.info("Initial Data Sample:")
            logging.info(self.df.head())
        except Exception as e:
            logging.error(f"Error during initial exploration: {e}")

# Example usage
# df = pd.read_csv("your_file.csv")
# optimizer = DataOptimizer(df)
# optimizer.initial_exploration()

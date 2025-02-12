import logging
import timeit
import functools

logging.basicConfig(
    format="{asctime} - {levelname} - {message}",
    style="{", 
    datefmt="%Y-%m-%d %H:%M", 
    level=logging.INFO
)

def time_execution(func):
    """Decorator to measure execution time of a function."""
   
def memory_usage(func):
    """Decorator to measure memory usage of a pandas DataFrame."""

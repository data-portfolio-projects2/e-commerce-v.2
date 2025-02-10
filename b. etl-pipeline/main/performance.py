logging.basicConfig(
    format="{asctime} - {levelname} - {message}",
    style="{", 
    datefmt="%Y-%m-%d %H:%M", 
    level=logging.INFO
)

def time_execution(func):
    """Decorator to measure execution time of a function."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = timeit.default_timer()  
        result = func(*args, **kwargs)       
        end_time = timeit.default_timer()    
        print(f"Function '{func.__name__}' executed in {end_time - start_time:.4f} seconds")
        return result
    return wrapper

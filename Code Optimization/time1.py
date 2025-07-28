import time

def timeit_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Function '{func.__name__}' executed in {execution_time:.6f} seconds")
        return result  # This was missing!
    return wrapper  # This was also missing!

@timeit_decorator
def example_function(n):
    total = 0
    for i in range(n):
        total += i ** 2
    return total

example_function(1000000)

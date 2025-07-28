from sitecustomize import timeit_decorator


@timeit_decorator
def example_function(n):
    total = 0
    for i in range(n):
        total += i ** 2
    return total


example_function(10000000)

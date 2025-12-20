import time


def fib1(n: int) -> int:
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


# First run computes and stores results
t0 = time.perf_counter()
print(fib1(750))
t1 = time.perf_counter()
print(f"First call took: {t1 - t0:.6f}s")

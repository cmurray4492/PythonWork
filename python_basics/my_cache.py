from functools import cache
import time


def fib1(n: int) -> int:
    if n < 2:
        return n
    return fib1(n - 1) + fib1(n - 2)


# First run computes and stores results
t0 = time.perf_counter()
print(fib1(35))
t1 = time.perf_counter()
print(f"First call took: {t1 - t0:.6f}s")


@cache
def fib(n: int) -> int:
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


# First run computes and stores results
t0 = time.perf_counter()
print(fib(35))
t1 = time.perf_counter()
print(f"First call took: {t1 - t0:.6f}s")

# Second run reuses the cached result (near-instant)
t0 = time.perf_counter()
print(fib(35))
t1 = time.perf_counter()
print(f"Second call took: {t1 - t0:.6f}s")

# You can inspect cache stats and clear it
print(fib.cache_info())   # hits, misses, size, etc.

fib.cache_clear()

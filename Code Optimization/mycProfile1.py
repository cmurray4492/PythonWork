import cProfile


def process_data(n):
    result = [x**2 for x in range(n)]
    return sum(result)


def main():
    process_data(10000000)


cProfile.run('main()')

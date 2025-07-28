"""Timed counting test"""

import time


def time_test_1():
    """Time Test Example"""
    start_time = time.time()

    counter = 0
    while counter < 1000000000:
        counter += 1

    end_time = time.time()

    total_time = end_time - start_time

    print("\n")
    print(f'Complete! Total Time: {total_time}')
    print("\n")


def main():
    """Main funmction to measure function execute time."""
    time_test_1()


if __name__ == '__main__':
    main()

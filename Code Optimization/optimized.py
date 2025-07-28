import time
from collections import defaultdict


def process_file(filename):
    word_counts = defaultdict(int)
    with open(filename, 'r') as file:
        for line in file:
            words = line.lower().split()
            for word in words:
                word_counts[word] += 1
    return word_counts


if __name__ == "__main__":
    start_time = time.time()
    counts = process_file('large_text_file.txt')
    print(f'Execution time: {time.time() - start_time} seconds')
    print(counts)

import time


def process_file(filename):
    word_counts = {}
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            words = line.strip().split()
            for word in words:
                word = word.lower()
                if word in word_counts:
                    word_counts[word] += 1
                else:
                    word_counts[word] = 1
    return word_counts


if __name__ == "__main__":
    start_time = time.time()
    counts = process_file('large_text_file.txt')
    print(f'Execution time: {time.time() - start_time} seconds')
    print(counts)

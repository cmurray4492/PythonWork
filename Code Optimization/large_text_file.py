import random


def generate_large_text_file(filename, num_lines):
    words = [
        'python', 'code', 'optimization', 'performance', 'bottleneck',
        'profiling', 'algorithm', 'data', 'process', 'function', 'variable',
        'loop', 'memory', 'speed', 'efficient', 'compute', 'analysis', 'test',
        'debug', 'system'
    ]
    with open(filename, 'w') as f:
        for _ in range(num_lines):
            line = ' '.join(random.choices(words, k=random.randint(5, 15)))
            f.write(line + '\n')


if __name__ == "__main__":
    generate_large_text_file('large_text_file.txt', 5000000)

import random

def gen_random(num_count, begin, end):
    result = []

    for _ in range(num_count):
        result.append(random.randint(begin, end))

    return result

if __name__ == "__main__":
    print(gen_random(5, 1, 3))
    print(gen_random(4, 9, 20))
import random

seq = [random.randint(1, 100) for i in range(100)]

def main(seq, func):
    tmp = 0
    for item in seq:
        tmp += func(item)
    return tmp

def num_pow(n):
    return n ** 2

x = main(seq, num_pow)

print(x)
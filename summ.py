import random

seq_1 = [random.randint(1, 100) for i in range(100)]
seq_2 = (i for i in range(100))

def main(seq, func):
    return sum(func(i) for i in seq)

def num_pow(n):
    return n ** 2

def num_div(n):
    return n // 2

print(main(seq_1, num_pow))
print(main(seq_2, num_div))

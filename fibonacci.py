import time

def fibonacci(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n > 2:
        return fibonacci(n - 1) + fibonacci(n - 2)


def get_fibonacci():
    storage = {}
    first_number = 0
    second_number = 1

    def calculation (n):
        nonlocal first_number
        nonlocal second_number

        if n in storage:
            return storage[n]
        elif n == 1:
            storage[n] = 0
        elif n == 2:
            storage[n] = 1
        else:
            next_number = first_number + second_number
            first_number = second_number
            second_number = next_number
            storage[n] = next_number
        return storage[n]
    return calculation

start_1 = time.time()

for i in range(1, 35):
    print(fibonacci(i))

print(f'Time: {time.time() - start_1}')
print('---------------------------------')

x = get_fibonacci()

start_2 = time.time()

for i in range(1, 35):
    print(x(i))

print(f'Time: {time.time() - start_2}')

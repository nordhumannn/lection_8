import timeit

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

print(timeit.timeit('fibonacci(30)', number = 5, setup='from __main__ import fibonacci'))
x = get_fibonacci()
print(timeit.timeit('x(30)', number=5, setup='from __main__ import x'))

#-------------------------------------------------------------------------

def fibonacci():
	numbers = [0, 1]
	
	def get_number(n):
		if n < len(numbers):
			return numbers[n]
		
		curr_item, next_item = numbers[-2], numbers[-1]
		
		i = len(numbers)
		
		while i <= n:
			curr_item, next_item = next_item, curr_item + next_item
			numbers.append(next_item)
			i += 1
		return next_item
		
	return get_number 

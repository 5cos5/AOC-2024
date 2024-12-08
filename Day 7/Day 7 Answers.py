import timeit

start = timeit.default_timer()

def possible_values(numbers):
	assert len(numbers) > 0
	if len(numbers) == 1:
		return {numbers[0]}
	
	result = set()
	for possible_value in possible_values(numbers[:-1]):
		result.add(possible_value + numbers[-1])
		result.add(possible_value * numbers[-1])
		result.add(int(f'{possible_value}{numbers[-1]}'))
	return result

equations = [(int(test_value), list(map(int, numbers.split(' ')))) for test_value, numbers in [equation.split(': ') for equation in open('Day 7/data.txt').read().splitlines()]]
print(sum([test_value for test_value, numbers in equations if test_value in possible_values(numbers)]))
print("The difference of time is :",
              timeit.default_timer() - start)
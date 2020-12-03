def smallest_multiple(factors):
	factors = list(factors)
	unique_factors = [n for i, n in enumerate(factors) if len([n%f for f in factors if not n%f]) != 1]

	print(unique_factors)

	total = 1
	for n in unique_factors:
		total *= n

	return total

# print(smallest_multiple(range(2, 20)))

def lcm(a, b):
	a1 = min([a, b])
	while a1%max([a, b]):
		a1 += a
	return a1

print(lcm(2, 4))
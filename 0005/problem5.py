def smallest_multiple(factors):
	factors = list(factors)
	lowest = lcm(*factors[:2])
	for n in factors[2:]:
		lowest = lcm(n, lowest)

	return lowest

def lcm(a, b):
	a1 = a
	while a1%b:
		a1 += a
	return a1

print(smallest_multiple(range(1, 21)))
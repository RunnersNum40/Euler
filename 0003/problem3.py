def factor(n):
	max_factor = 1

	#iterate though all the odd integers as well as 2 and divide n by any that factor n
	#because we will find the primes earlier than any of the multiples of that prime we will never find a non-prime that divides n
	for f in [2]+list(range(3, int(n**(0.5))+2, 2)):
		while n%f == 0:
			n //= f
			max_factor = f

	#if n is still greater than 2 it is prime itself
	if n > 2:
		max_factor = n

	return max_factor

print(factor(600851475143))
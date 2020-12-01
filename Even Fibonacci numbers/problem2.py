def even_fib(n1=0, n2=2, limit=4000000):
	if max(n1, n2) > limit:
		return 0

	n1, n2 = n2, 4*n2+n1

	return even_fib(n1, n2)+n1

print(even_fib())
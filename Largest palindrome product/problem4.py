def is_palendrome(n):
	return str(n) == str(n)[::-1]

def palindrome_product(digits=3):
	min_num = 10**(digits-1)
	max_num = 10**digits-1

	colec = []

	for n in range(max_num, min_num, -1):
		for i in range(n+11-n%11, min_num, -11 if n%11 else -1):
			if is_palendrome(n*i) and i<=max_num:
				colec.append(n*i)

	return max(colec)

print(palindrome_product(3))
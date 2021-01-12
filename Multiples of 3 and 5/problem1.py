limit = 1000
factors = (3, 5)

n = sum(x for x in range(0, limit, int(limit/abs(limit))) if any(x%factor == 0 for factor in factors))
print(n)


n = sum(set(range(3, 1001, 3))|set(range(5, 1001, 5)))
print(n)
limit = 1000
factors = (3, 5)

n = sum(x for x in range(0, limit, int(limit/abs(limit))) if any(x%factor == 0 for factor in factors))

print(n)
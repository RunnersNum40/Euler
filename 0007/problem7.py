def is_prime(n, primes):
    if n <= 1:
        return False
    for factor in primes:
        if n%factor == 0:
            return False
    else:
        return True

def find_prime(nth):
    n, primes = 0, [2]
    while nth > 1:
        n += 1
        if is_prime(n, primes):
            nth -= 1
            primes.append(n)

    return n

print(find_prime(10001))
from math import sqrt

def factors_of(n):
    """Find all the integer factors of n"""
    for i in range(2, int(sqrt(n))):
        if n%i == 0:
            yield(i)
            if i != n/i:
                yield(n/i)

def special_pythagorean_triplet(n):
    """Find the pythagorean triplet that sums to n and return it's product"""
    for a in factors_of(n):
        # For each factor find b such that a^2+b^2 = (1000-a-b)^2
        b = (n/2-a)/(1-a/n)
        # For the a and b find c
        c = n-a-b
        # Check if the triplet is valid
        if a<b<c and b==int(b):
            return(int(a*b*c))

print(special_pythagorean_triplet(1000))
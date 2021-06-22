#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

bool is_prime(int n, int* primes, int n_primes) {
    if(n <= 1) {
        return false;
    }
    if(n_primes < 1) {
        return true;
    }
    for(int i = 0; i < n_primes; i++) {
        if(n%primes[i] == 0) {
            return false;
        }
    }
    return true;
}

int find_prime(int nth) {
    int n = 0;
    int i = 0;
    int primes[nth];
    while(nth >= 1) {
        n += 1;
        if(is_prime(n, primes, i)) {
            nth -= 1;
            primes[i] = n;
            i++;
        }
    }
    return n;
}

int main() {
    printf("%d\n", find_prime(10001));
}
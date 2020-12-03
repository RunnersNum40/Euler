#include <stdio.h>
#include <math.h>

int main() {
	long long int n = 600851475143;
	int max_factor = 1;

	while(n%2 == 0) {
		n /= 2;
		max_factor = 2;
	}

	int i;
	for(i = 3; i <= (int)sqrt((long double)n)+1; i++) {
		while(n%i == 0) {
			n /= i;
			max_factor = i;
		}
	}

	printf("%d\n", max_factor);
}
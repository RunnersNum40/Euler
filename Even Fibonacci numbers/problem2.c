#include <stdio.h>

int even_fib(int n1, int n2, int limit) {
	if(n2 > limit) {
		return n2;
	}

	n3 = 4*n2+n1;
	
	n1 = n2;
	n2 = n3;

	return even_fib(n1, n2, limit)+n1;
}

int main() {
	int n = even_fib(0, 2, 4000000);
	printf("%d\n", n);
}
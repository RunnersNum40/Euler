#include <stdio.h>
#include <math.h>

int intPow(int x, int y) {
	//return the integer result of (int) x ^ (int) y
	return (int) pow((double)x, (double)y);
}

int square_sum_diff(int n) {
	return (3*intPow(n, 4)+2*intPow(n, 3)-3*intPow(n, 2)-2*n)/12;
}

int main() {
	printf("%d\n", square_sum_diff(100));
}
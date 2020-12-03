#include <stdio.h>
#include <math.h>
#include <stdbool.h> 


bool is_palindrome(int n) {
	int digits = (int)log10(n);

	int i;
	for(i = 0; i < digits/2; i++) {
		if((n/(int)pow(10, i))%10 != (n/(int)pow(10, digits-i))%10) {
			return false;
		}
	}
	return true;
}

int main() {
	int digits = 3;

	int min_num = (int) pow(10, digits-1);
	int max_num = max_num*10-1;

	int i, j;
	for(i = max_num; i > min_num; i--) {
		for(j = i; j > min_num; j--) {
			
		}
	}
}
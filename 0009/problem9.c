#include <stdio.h>
#include <math.h>

int check(int a, int n) {
    //Check if a given a and n pair can work for a^2+b^2=c^2 where a+b+c=n
    float a_f = (float) a;
    float n_f = (float) n;
    float b = (n_f/2-a_f)/(1-a_f/n_f);
    if(b == (int)b) {
        int c = n-a-b;
        if(a<b && b<c) {
            return a*b*c;
        }
    }
    return 0;
}

int special_pythagorean_triplet(int n) {
    //Find all the integer factors of n
    int soln;
    for (int a = 1; a <= sqrt(n); a++) {
        if (n%a == 0) {
            if (n/a == a) {
                if(soln = check(a, n))
                    return soln;
            }
            else {
                if(soln = check(n/a, n))
                    return soln;
            }
        }
    }
}

int main() {
    printf("%d\n", special_pythagorean_triplet(1000));
}
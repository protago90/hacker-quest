// by protago90

#include "utils.h"
#include <math.h>


int run_e7v1(int x) {
    int i = 0, n = 0;
    for (n; ; n++) {
        if (is_prime(n)) {
            i += 1;
            if (x == i) { return n; } 
        }
    }
    return 0;
}


int solve_e7() {
    /**
    * 10001st
    * By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that
    * the 6th prime is 13.
    * > What is the 10 001st prime number?
    **/
    return run_e7v1(10001); 
}


/** int main() {
    promptify(solve_e7, 7);
    // >> the anwser for the #7 euler problem is >104743<; computed in 0.0148s ∎
    return 0;
}*/
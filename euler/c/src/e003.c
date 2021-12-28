// by protago90

#include "utils.h"
#include <math.h>


int run_e3v1(long x) {
    long lim = sqrt(x);
    long n;
    for (n = lim; n > 1; n--) {
        if (x % n == 0) {
            if (is_prime(n)) { return n; }
        }
    }
    return 0;
}


long solve_e3() {
    /**
    * Largest prime factor
    * The prime factors of 13195 are 5, 7, 13 and 29.
    * > What is the largest prime factor of the number 600851475143 ?
    **/
    return run_e3v1(600851475143); 
}


// int main() {
//     promptify(solve_e3, 3);
//     // >> the anwser for the #3 euler problem is >6857<; computed in 0.0069s ∎
//     return 0;
// }
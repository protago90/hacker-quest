// by protago90

#include "utils.h"
#include <math.h>


long run_e10v1(int x) {
    long rec = 0;
    long n = 0;
    for (n; n < x; n++) {
        if (is_prime(n)) { rec += n; }
    }
    return rec;
}


long solve_e10() {
   /***
    * Summation of primes
    * The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
    * > Find the sum of all the primes below two million.
    **/
    return run_e10v1(2000000); 
}


// int main() {
//     promptify(solve_e10, 10);
//  // >> the anwser for the #10 euler problem is >142913828922<; computed in 0.5873s ∎
//     return 0;
// }
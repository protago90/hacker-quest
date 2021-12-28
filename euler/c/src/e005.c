// by protago90

#include "utils.h"
#include <math.h>


int run_e5v1(int x) {
    int p = 1;
    int rec[LIM] = {0};
    int n = 2;
    for (n; n <= x; n++) {
        int i = 0;
        int pf[LIM] = {0};
        prime_factors(n, pf);
        for (i; i <= x; i++) {
            rec[i] += MAX(pf[i] - rec[i], 0);
        }
    }
    int i = 0;
    for (i; i <= x; i++) {
        p *= MAX(pow(i, rec[i]), 1); 
    }
    return p;
}


long solve_e5() {
   /***
    * Smallest multiple
    * 2520 is the smallest number that can be divided by each of the numbers from
    * 1 to 10 without any remainder.
    * > What is the smallest positive number that is evenly divisible by all of 
    * the numbers from 1 to 20?
    **/
    return run_e5v1(20); 
}


// int main() {
//     promptify(solve_e5, 5);
//  // >> the anwser for the #5 euler problem is >232792560<; computed in 0.0065s ∎
//     return 0;
// }
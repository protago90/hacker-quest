// by protago90

#include "utils.h"
#include <math.h>


int run_e4v1(int x) {
    int rec = 1;
    int p_rev, p;
    int lim = pow(10, x) - 1;
    int n   = pow(10, x-1);
    int m;
    for (n; n < lim; n++) {
        for (m = n; m < lim; m++) {
            int tmp = n*m;
            p = tmp;
            p_rev = 0;
            while (tmp != 0) {
                p_rev = p_rev*10 + tmp % 10;
                tmp /= 10;
            }
            if (p == p_rev && p > rec) { rec = p; }
        }
    } 	
    return rec;
}


long solve_e4() {
   /***
    * Largest polindrome product
    * A palindromic number reads the same both ways. The largest palindrome made from
    * the product of two 2-digit numbers is 9009 = 91 × 99.
    * > Find the largest palindrome made from the product of two 3-digit numbers.
    **/
    return run_e4v1(3); 
}


// int main() {
//     promptify(solve_e4, 4);
//  // >> the anwser for the #4 euler problem is >906609<; computed in 0.0111s ∎
//     return 0;
// }
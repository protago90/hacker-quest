// by protago90

#include "utils.h"
#include <math.h>



int run_e9v1(int x) {
    int lim = x/2;
    int a, b;
    double c;
    for (a = 1; a < lim; a++) {
        for (b = 1; b < a; b++) {
            c = sqrt(pow(a, 2) + pow(b, 2));
            if (a + b + c == x) { return a*b*c; }
        }
    }
    return 0;
}


int solve_e9() {
   /***
    * Special Pythagorean triplets
    * A Pythagorean triplet is a set of three natural numbers, a < b < c, for which
    * a^2 + b^2 = c^2. For example 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
    * > There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    * Find the product abc.
    **/
    return run_e9v1(1000); 
}


/** int main() {
    promptify(solve_e9, 9);
    // >> the anwser for the #9 euler problem is >31875000<; computed in 0.0054s ∎
    return 0;
}*/
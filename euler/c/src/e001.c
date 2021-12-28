// by protago90

#include "utils.h"


int run_e1v1(int x) {
    int rec = 0;
    int i;
    for (i; i < x; i++) {
        if (i % 3 == 0 || i % 5 == 0) { rec += i; }
    }
    return rec;
}


int solve_e1() {
    /**
    * Multiples of 5 and 3
    * If we list all the natural numbers below 10 that are multiples of 3 or 5,
    * we get 3, 5, 6 and 9. The sum of these multiples is 23.
    * > Find the sum of all the multiples of 3 or 5 below 1000. 
    **/
    return run_e1v1(1000);
}


/** int main() {
    promptify(solve_e1, 1);
    // >> the anwser for the #1 euler problem is >233168<; computed in 0.0000s ∎
    return 0;
}*/
// by protago90

#include "utils.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <time.h>


/* Utils */

void promptify(long (*func)(), int n) {
    /**
    * Handler of euler's problem dedicated [func] to print solution and computing time. 
    **/
    clock_t t;
    double tt;
    long anwser;
    t = clock();
    anwser = func();
    tt = ((double) clock() - t)/CLOCKS_PER_SEC;  
    printf("  >> the anwser for the #%d euler problem is >%ld<; ", n, anwser);
    printf("computed in %0.4fs ∎\n", tt);
}


/* Commons */   

void prime_factors(int x, int *rec) {
    /**
    * Produce prime factors aka prime decomposition of [x] numb.
    **/
    while (x != 1) {
        int n = 2;
        for (n; n <= x; n++) {
            if ((x % n == 0) & is_prime(n)) {
                rec[n] += 1; x = x/n;
            }
        }
    }
}

void factors(long x, long *rec) {
    /**
    * Produce all factors of considered [x] numb.
    **/
    long n = 1, i = 0;
    for(n; n <= x; n++) {
        if (x % n == 0) { rec[i] = n; i++; }
    }
}

int is_prime(long x) {
    /**
    * Test if given [x] numb belongs to the primes.
    **/
    if ((x < 2) | (x > 2 & x % 2 == 0)) { 
        return 0; 
    }
    // ver1
    long lim = sqrt(x);
    long n = 3;
    for (n; n <= lim; n += 2) {
        if (x % n == 0) { return 0; } 
    }
    return 1;
    // ver2 --slowish
    // long rec[LIM]; 
    // // ? = malloc(LIM*sizeof(*rec));
    // factors(x, rec);
    // if (rec[0] == 1 & rec[1] == x) { return 1; }
    // return 0;
}
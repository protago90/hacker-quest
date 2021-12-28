// by protago90

#ifndef _UTILS_H
#define _UTILS_H

 #define LIM 1000000
 #define MAX(x, y) (((x) > (y)) ? (x) : (y))

    void promptify(long (*solver)(), int n);

     int is_prime(long x);
    void factors(long x, long *rec);
    void prime_factors(int x, int *rec);

#endif
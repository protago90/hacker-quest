// by protago90

#include <stdio.h>
#include <time.h>
#include <string.h>


/** Utils **/

void promptify(int (*solver)(), int n) {
    clock_t t;
    double tt;
    int anwser;
    t = clock();
    anwser = solver();
    tt = ((double) clock() - t)/CLOCKS_PER_SEC; 
    printf("  >> the anwser for the #%d euler problem is >%d<; ", n, anwser);
    printf("computed in %0.4fs ∎\n", tt);
}
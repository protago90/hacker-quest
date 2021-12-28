// by protago90

#include <stdio.h>
#include <stdlib.h>
#include "utils.h"
#include "eall.h"  // i.e. all solvers from src/E??.c


void run_solver(int n) {
    long (*solve)();
    switch (n) {
        case 1:  solve = solve_e1;  break;   // Multiples of 5 and 3
        case 2:  solve = solve_e2;  break;   // Even Fibonacci numbers
        case 3:  solve = solve_e3;  break;   // Largest prime factor
        case 4:  solve = solve_e4;  break;   // Largest polindrome product
        case 5:  solve = solve_e5;  break;   // Smallest multiple
        case 6:  solve = solve_e6;  break;   // Sum square difference
        case 7:  solve = solve_e7;  break;   // 10001st
        case 8:  solve = solve_e8;  break;   // Largest product in a series	
        case 9:  solve = solve_e9;  break;   // Special Pythagorean triplets
        case 10: solve = solve_e10; break;   // Summation of primes  
        default: 
            printf("  >> given euler problem is not valid\n"); return;
    }
    promptify(solve, n);
}


int main (int argc, char *argv[]) {
    if (argc <= 1) {
        printf("  >> specify #n euler problem\n"); return 0;
    }
    int euler_problem = atoi(argv[1]); 
    run_solver(euler_problem);
    return 0;
}
// by protago90

#include <stdio.h>
#include <stdlib.h>
#include "utils.h"
#include "eall.h"  // i.e. all solvers from src/E??.c


void run_solver(int n) {
	switch (n) {
		case 1:  promptify(solve_e1, n);  break;   // Multiples of 5 and 3
		default: 
			printf("  >> given euler problem is not valid\n"); break;
	}
}


void main (int argc, char *argv[]) {
	if (argc <= 1) {
		printf("  >> specify #n euler problem\n");  exit(1);
	}
	int euler_problem = atoi(argv[1]); 
	run_solver(euler_problem);
}
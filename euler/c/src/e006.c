// by protago90

#include "utils.h"
#include <math.h>


int run_e6v1(int x) {
    int sq_s = 0;
    int s_sq = 0;
    int n;
    for (n; n <= x; n++) {
        sq_s += n;
        s_sq += pow(n, 2);	
    }
    sq_s = pow(sq_s,2);
    return sq_s - s_sq;
}


long solve_e6() {
   /***
    * Sum square difference
    * The sum of the squares of the first ten natural numbers is
    * 1^2 + 2^2 + ... + 10^2 = 385.
    * The square of the sum of the first ten natural numbers is
    * (1 + 2 + ... + 10)^2 = 55^2 = 3025.
    * Hence the difference between the sum of the squares of the first ten natural
    * numbers and the square of the sum is 3025 − 385 = 2640.
    * > Find the difference between the sum of the squares of the first one hundred
    * natural numbers and the square of the sum.
    **/
    return run_e6v1(100); 
}


// int main(){
//     promptify(solve_e6, 6);
//  // >> the anwser for the #6 euler problem is >25164150<; computed in 0.0001s ∎
//     return 0;
// }
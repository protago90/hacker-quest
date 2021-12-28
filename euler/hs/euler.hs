-- by protago90

import Src.Utils (promptify, Solver)
import Src.EALL  -- i.e. all solvers from src/E*.hs
import System.Environment   


getSolver :: String -> Solver
getSolver "1"  = solverE1   -- Multiples of 5 and 3
getSolver "2"  = solverE2   -- Even Fibonacci numbers
getSolver "3"  = solverE3   -- Largest prime factor TODO
getSolver "4"  = solverE4   -- Largest polindrome product
getSolver "5"  = solverE5   -- Smallest multiple TODO
getSolver "6"  = solverE6   -- Sum square difference
getSolver "7"  = solverE7   -- 10001st
getSolver "8"  = solverE8   -- Largest product in a series TODO
getSolver "9"  = solverE9   -- Special Pythagorean triplets
getSolver "10" = solverE10  -- Summation of primes
getSolver _ = error "  >> given euler problem is not valid"


main = do
    args <- getArgs
    if null args
       then putStrLn "  >> specify #n euler problem"
       else let eulerProblem = head args in promptify $ getSolver eulerProblem
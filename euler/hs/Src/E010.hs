-- by protago90
module Src.E010 where

import Src.Utils (promptify, Solver(..), genPrimes)


runE10 :: Integral a => a -> a
runE10 x = sum $ takeWhile (<x) $ genPrimes [2..]


solverE10 = Solver 10 runE10 2000000
{-- Summation of primes
    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
    > Find the sum of all the primes below two million. --}


main = do
    promptify solverE10
 -- >> the anwser for the #10 euler problem is >142913828922<; computed in ?.???? ∎
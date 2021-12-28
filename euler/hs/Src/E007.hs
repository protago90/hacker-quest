-- by protago90
module Src.E007 where

import Src.Utils (promptify, Solver(..), genPrimes)


runE7 :: Integral a => a -> a
runE7 x = last $ (take . fromIntegral) x $ genPrimes [2..]


solverE7 = Solver 7 runE7 10001
{-- 10001st
    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that
    the 6th prime is 13.
    > What is the 10 001st prime number? --}


main = do
    promptify solverE7
 -- >> the anwser for the #6 euler problem is >104743<; computed in 0.0000s ∎
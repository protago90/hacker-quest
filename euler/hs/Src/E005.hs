-- by protago90
module Src.E005 where

import Src.Utils (promptify, Solver(..), genPrimeFactors, factorize)
import Data.List ((\\), genericDrop)


runE5 :: Integral a => a -> a
runE5 x = product $ foldl1 cumDiff $ map decompose [1..x]
    where decompose n   = factorize n $ genPrimeFactors n
          cumDiff xs ys = xs ++ (ys \\ xs)
          
runE5' :: Integral a => a -> a
runE5' x = foldl1 lcm [1..x] --to much 'batteries-included' ^^


solverE5 = Solver 5 runE5 20
{-- Smallest multiple
    2520 is the smallest number that can be divided by each of the numbers from
    1 to 10 without any remainder.
    > What is the smallest positive number that is evenly divisible by all of
    the numbers from 1 to 20? --}


main = do
    promptify solverE5
 -- >> the anwser for the #5 euler problem is >232792560<; computed in 0.0000s ∎
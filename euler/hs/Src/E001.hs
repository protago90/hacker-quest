-- by protago90
module Src.E001 where

import Src.Utils (promptify, Solver(..))


isDivBy3or5 :: Integral a => a -> Bool
isDivBy3or5 x = x `mod` 3 == 0 || x `mod` 5 == 0


runE1 :: Integral a => a -> a
runE1 x = sum [n | n <- [1..x-1], isDivBy3or5 n]

runE1' :: Integral a => a -> a
runE1' x = foldl (\acc n -> if p n then n + acc else acc) 0 [1..x-1]
    where p = isDivBy3or5


solverE1 = Solver 1 runE1 1000
{-- Multiples of 5 and 3
    If we list all the natural numbers below 10 that are multiples of 3 or 5,
    we get 3, 5, 6 and 9. The sum of these multiples is 23.
    > Find the sum of all the multiples of 3 or 5 below 1000. --}


main = do
    promptify solverE1
 -- >> the anwser for the #1 euler problem is >233168<; computed in 0.000s ∎
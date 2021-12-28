-- by protago90
module Src.E004 where

import Src.Utils (promptify, Solver(..))


isPolindrome :: (Show a, Integral a) => a -> Bool
isPolindrome x = show x == (reverse . show) x

genProds :: Integral a => a -> a -> [a] 
genProds x y = [n*m | n <- [x..y], m <- [n..y]]


runE4 :: (Show a, Integral a, Integral b) => b -> a
runE4 x = foldl (\acc prod -> if p prod acc then prod else acc) 0 $ genProds t0 tn
    where p n m    = isPolindrome n && n > m
          (t0, tn) = (10^(x-1), 10^x - 1)


solverE4 = Solver 4 runE4 3
{-- Largest polindrome product
    A palindromic number reads the same both ways. The largest palindrome made
    from the product of two 2-digit numbers is 9009 = 91 × 99.
    > Find the largest palindrome made from the product of two 3-digit numbersi. --}


main = do
    promptify solverE4
 -- >> the anwser for the #4 euler problem is >906609<; computed in 0.0000s ∎
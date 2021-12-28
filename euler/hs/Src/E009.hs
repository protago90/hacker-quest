-- by protago90
module Src.E009 where

import Src.Utils (promptify, Solver(..))


runE9 :: (Integral a) => a -> a
runE9 x = head [a*b*c | c <- [1..x], b <- [1..c], a <- [1..b], p a b c]
    where p a b c = a^2 + b^2 == c^2 && a+b+c == x


solverE9 = Solver 9 runE9 1000
{-- Special Pythagorean triplets
    A Pythagorean triplet is a set of three natural numbers, a < b < c, for which
    a^2 + b^2 = c^2. For example 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
    > There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    Find the product abc. --}


main = do
    promptify solverE9
 -- >> the anwser for the #9 euler problem is >31875000<; computed in 0.0000s ∎
-- by protago90
module Src.E006 where

import Src.Utils (promptify, Solver(..))


runE6 :: Integral a => a -> a
runE6 x = (^2) (sum [1..x]) - sum (map (^2) [1..x])


solverE6 = Solver 6 runE6 100
{-- Sum square difference
    The sum of the squares of the first ten natural numbers is
    1^2 + 2^2 + ... + 10^2 = 385.
    The square of the sum of the first ten natural numbers is
    (1 + 2 + ... + 10)^2 = 55^2 = 3025.
    Hence the difference between the sum of the squares of the first ten natural
    numbers and the square of the sum is 3025 − 385 = 2640.
    > Find the difference between the sum of the squares of the first one hundred
    natural numbers and the square of the sum. --}


main = do
    promptify solverE6
 -- >> the anwser for the #6 euler problem is >25164150<; computed in 0.0000s ∎
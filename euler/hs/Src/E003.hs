-- by protago90
module Src.E003 where

import Src.Utils (promptify, Solver(..), isPrime)


-- below ~Eratosthenes primes approach is overhelmingly slow.. 
-- genDescPrimes :: Integral a => a -> [a]
-- genDescPrimes x = foldl f [] [2..x+1]
--    where f = (\acc n -> if p n acc then acc else n:acc)
--          p z zs = any ((==0) . (z `mod`)) zs

-- runE3' :: Integral a => a -> a
-- runE3' x = head $ filter p $ reverse $ genDescPrimes lim
--     where lim = (floor . sqrt . fromIntegral) x
--           p n = x `mod` n == 0

runE3 :: Integral a => a -> a
runE3 x = head $ filter isPrime revFactors
    where revFactors = [ n | n <- [lim, lim-1..1], x `mod` n == 0]
          lim        = (floor . sqrt . fromIntegral) x


solverE3 = Solver 3 runE3 600851475143
{-- Largest prime factor
    The prime factors of 13195 are 5, 7, 13 and 29.
    > What is the largest prime factor of the number 600851475143 ? --}


main = do
    promptify solverE3
 -- >> the anwser for the #3 euler problem is >6857<; computed in 0.0000s ∎
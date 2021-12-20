-- by protago90
module Src.Utils (
    promptify, Solver(..), genPrimes, isPrime, genPrimeFactors, factorize) where

import System.CPUTime (getCPUTime)
import Text.Printf (printf)


-- UTILS

data Solver = Solver {
   getN :: Int, getFunc :: Integer -> Integer, getX :: Integer }

-- Handler of euler's problem dedicated [s]olver that print solution and computing time.
promptify :: Solver -> IO ()
promptify s = do
    t <- getCPUTime
    let n = getN s
    let anwser = getFunc s $ getX s
    tt <- getCPUTime
    printf "  >> the anwser for the #%d euler problem is >%d<; " n anwser
    printf "computed in %0.4fs ∎\n" (fromIntegral (tt - t) / (10^12) :: Double)


-- COMMONS

genPrimes :: Integral a => [a] -> [a]
genPrimes [] = []
genPrimes (x:xs)
    | x < 2     = genPrimes xs
    | otherwise = x : genPrimes (filter (\n -> n `mod` x /= 0) xs)

isPrime :: Integral a => a -> Bool
isPrime x = genFactors x == [1, x]

genFactors :: Integral a => a -> [a]
genFactors x = [n | n <- [1..x], x `mod` n == 0]

genPrimeFactors :: Integral a => a -> [a]
genPrimeFactors x = filter isPrime $ genFactors x

factorize :: (Integral a) => a -> [a] -> [a]
factorize _ [] = []
factorize 1 _  = []
factorize x pFactors@(p:ps)
    | x `mod` p == 0 = p :factorize (x `div` p) pFactors
    | otherwise      = factorize x ps
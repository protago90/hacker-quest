-- by protago90
module Src.Utils (
    promptify, Solver(..)) where

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
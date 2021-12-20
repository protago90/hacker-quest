-- by protago90

import Src.Utils (promptify, Solver)
import Src.EALL  -- i.e. all solvers from src/E??.hs
import System.Environment   


getSolver :: String -> Solver
getSolver "1"  = solverE1   -- Multiples of 5 and 3
getSolver _ = error "  >> given euler problem is not valid"


main = do
    args <- getArgs
    if null args
       then putStrLn "  >> specify #n euler problem"
       else let eulerProblem = head args in promptify $ getSolver eulerProblem
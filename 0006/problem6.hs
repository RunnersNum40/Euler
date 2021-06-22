squareSumDiff :: Integer -> Integer
squareSumDiff n = (3*n^4+2*n^3-3*n^2-2*n) `div` 12

main :: IO()
main = print(squareSumDiff 100)
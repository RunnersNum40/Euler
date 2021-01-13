factor :: Integer -> Integer -> Integer
factor n f
    | n `mod` f == 0 = factor (n `div` f) f
    | otherwise = n

maxFactor :: Integer -> Integer
maxFactor n = factors n 2
    where
        factors n i
            | n == 1 = i
            | otherwise = factors (factor n i) i+1

main :: IO()
main = print(maxFactor 600851475143)
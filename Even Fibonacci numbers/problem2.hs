sumFib :: Integer -> Integer
sumFib limit = sumFib' 0 2 0 limit

sumFib' :: Integer -> Integer -> Integer -> Integer -> Integer
sumFib' a b acc limit
    | b > limit = acc
    | otherwise = sumFib' b (4*b+a) newAcc limit
        where newAcc = b + acc

main :: IO()
main = print(sumFib(4000000)) 
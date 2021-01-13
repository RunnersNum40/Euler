fibSum :: Integer -> Integer -> Integer -> Integer
fibSum a b limit
    | b >= limit = 0
    | b < limit = b + (fibSum b (4*b+a) limit)

main :: IO()
main = print(fibSum 0 2 4000000)
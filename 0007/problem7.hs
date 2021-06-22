is_prime :: Integer -> [Integer] -> Bool
is_prime n (x:xs)
    | x == 1 = True
    | n `mod` x == 0 = False
    | otherwise = is_prime(n (xs))

find_prime :: Integer -> Integer -> [Integer] -> Integer
find_prime nth n primes
    | nth <= 1 = n
    | is_prime(n primes) = find_prime((nth-1) (n+1) (n:primes))
    | otherwise = find_prime(nth (n+1) primes)


main :: IO()
main = print(find_prime 10001 [1])
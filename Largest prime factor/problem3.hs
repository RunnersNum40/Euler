factor :: Integer -> Integer -> Integer
factor n f
	| n%f == 0 = factor (n/f) f
	| otherwise = n

main :: IO()
main = print(sumFib(4000000)) 
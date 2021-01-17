lcmm :: Integral a => [a] -> a
lcmm [] = 1
lcmm (x:xs) = lcm x (lcmm xs)

main :: IO()
main = print(lcmm [1..21])
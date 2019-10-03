#DP and bottom up approach
def Fibonacci_sequence(n):
    if n == 1 or n ==2:
        result = 1
    #the bottom up list stored previous calculation
    bottom_up = [None] * (n+1)
    bottom_up[1] = 1
    bottom_up[2] = 1
    for i in range(3,n+1):
        bottom_up[i] = bottom_up[i-1] + bottom_up[i-2]
    return bottom_up[n]

assert Fibonacci_sequence(35) == 9227465
assert Fibonacci_sequence(100) == 354224848179261915075

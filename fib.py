
memo = {}

def fib_recursion(n):
    if n < 2:
        return n
    if n in memo:
        return memo[n]

    memo[n] = fib_recursion(n-1) + fib_recursion(n-2)
    return memo[n]

def fib_dp(n):
    if n == 0:
        return 0

    prev,curr=0,1
    for i in range(2, n + 1):
        # s = prev + curr
        prev, curr=curr, prev + curr

    return curr

    # dp = {
    #     0:0,
    #     1:1,
    # }
    # for i in range(2, n + 1):
    #     dp[i] = dp[i-1] + dp[i-2]
    # return dp[n]

print(fib_dp(20))
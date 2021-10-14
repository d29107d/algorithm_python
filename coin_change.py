import sys

memo = {}
def change_recursion(coins, amount):
    if amount == 0:
        return 0
    if amount < 0:
        return -1
    if amount in memo:return memo[amount]
    res = sys.maxsize
    for coin in coins:
        sub_problem = change_recursion(coins, amount - coin)
        if sub_problem == -1:continue
        res = min(res, sub_problem+1)

    memo[amount] = -1 if res==sys.maxsize else res
    return memo[amount]

def change_dp(coins, amount):
    dp = {0:0}
    amount_max = amount+1
    for i in range(1, amount_max):
        m=amount_max
        for coin in coins:
            if i - coin < 0: continue
            dp[i] = min(m, 1 + dp[i - coin])
    return (dp[amount] == amount_max) and -1 or dp[amount]

# print(change_recursion([1, 2, 5], 20))
print(change_dp([1, 2, 5], 7))
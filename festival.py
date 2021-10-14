n = int(input())
r = int(input())
a = [int(input()) for i in range(n)]
# let dp[i][j] represent the money they can obtain if 
# week[i] is the jth consecutive tournament the participate in
dp = [[0]*(r+1) for i in range(n+1)]
for i in range(1, n+1):
    for j in range(r+1):
        if j==0 and i:
            dp[i][j] = max(dp[i-1])
        else:
            dp[i][j] = dp[i-1][j-1]+a[i-1]
print(max(dp[n]))
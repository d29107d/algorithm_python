'''
有这样一道智力题：“某商店规定：三个空汽水瓶可以换一瓶汽水。小张手上有十个空汽水瓶，她最多可以换多少瓶汽水喝？”答案是5瓶，
方法如下：先用9个空瓶子换3瓶汽水，喝掉3瓶满的，喝完以后4个空瓶子，用3个再换一瓶，喝掉这瓶满的，这时候剩2个空瓶子。然后你让
老板先借给你一瓶汽水，喝掉这瓶满的，喝完以后用3个空瓶子换一瓶满的还给老板。如果小张手上有n个空汽水瓶，最多可以换多少瓶汽水喝？
'''

# numOfBottle = int(input("Please input bottle number:"))

def calcBottle(num):
    change,left=0,num

    while 1:
        if left > 2:
            change += left // 3
            left = left % 3 + left // 3
        else:
            change += 1 if left == 2 else 0
            break

    return change

print(calcBottle(10))

n = int(input())
r = int(input())
a = [int(input()) for i in range(n)]
# let dp[i][j] represent the money they can obtain if
# week[i] is the jth consecutive tournament the participate in
dp = [[0]*(r+1) for i in range(n+1)]
# print(len(dp))
for i in range(1, n+1):
    for j in range(r+1):
        if j==0:
            dp[i][j] = max(dp[i-1])
        else:
            dp[i][j] = dp[i-1][j-1]+a[i-1]
        print(dp)
print(max(dp[n]))
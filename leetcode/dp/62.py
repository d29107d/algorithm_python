class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = {}

        def recursion(right: int, bottom: int) -> int:
            key = (right, bottom)
            if key in dp:
                return dp[key]

            if right == 1:
                dp[key] = 1
            elif bottom == 1:
                dp[key] = 1
            else:
                dp[key] = recursion(right - 1, bottom) + recursion(right, bottom - 1)

            return dp[key]

        return recursion(m, n)

# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
        # dp=[[-1 for i in range(n+1)] for i in range(m+1)]
        #
        # def helper(indm,indn):
        #     if indm==m-1 and indn==n-1:
        #         return 1
        #     if indm>=m or indn>=n:
        #         return 0
        #     if dp[indm][indn]!=-1:
        #         return dp[indm][indn]
        #     a=helper(indm+1,indn)+helper(indm,indn+1)
        #     dp[indm][indn]=a
        #     return dp[indm][indn]
        #
        # return helper(0,0)




s = Solution()
print(s.uniquePaths(23, 12))
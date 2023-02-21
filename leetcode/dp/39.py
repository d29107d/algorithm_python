from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [[] for _ in range(target + 1)]
        for c in candidates:  # O(N): for each candidate
            for i in range(c, target + 1):  # O(M): for each possible value <= target
                if i == c:
                    dp[i].append([c])
                for comb in dp[i - c]:  # O(M) worst: for each combination
                    dp[i].append(comb + [c])
        return dp[-1]

        # self dp ------------
        # def helper(total, memo={}):
        #     if total in memo:
        #         return memo[total]
        #
        #     if total == target:
        #         return [[]]
        #
        #     result = []
        #     for candidate in candidates:
        #         cur = total + candidate
        #         if cur > target:
        #             continue
        #
        #         ways = helper(cur, memo)
        #         for way in ways:
        #             result.append([candidate] + way)
        #
        #     memo[total] = result
        #     return result
        #
        # return helper(0)
        # self dp ------------

        # dfs ---------------
        # res = []
        #
        # def dfs(start, path):
        #     total = sum(path)
        #
        #     if start >= len(candidates) or len(candidates) == 0 or total > target:
        #         return
        #
        #     if total == target:
        #         res.append(path)
        #         return
        #
        #     # dfs(start, path + [candidates[start]])
        #     dfs(start + 1, path)
        #     dfs(start, path + [candidates[start]])
        #
        # dfs(0, [])
        # return res
        # dfs ---------------


s = Solution()
# print(s.combinationSum([2, 3, 6, 7], 7))
print(s.combinationSum([2, 3], 5))
# print(s.combinationSum([7, 14], 300))
# print(s.combinationSum([2, 3, 6, 10], 15))

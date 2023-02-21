from typing import List

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # self dp ------------
        # def helper(total, memo={}):
        #     if total in memo:
        #         return memo[total]
        #
        #     if total == target:
        #         return 1
        #
        #     ret = 0
        #     for num in nums:
        #         cur = num + total
        #         if cur > target:
        #             continue
        #
        #         ret += helper(cur, memo)
        #
        #     memo[total] = ret
        #     return ret
        # return helper(0)
        # self dp ------------

        # neetcode -----
        dp = {0: 1}

        for total in range(1, target + 1):
            dp[total] = 0
            for n in nums:
                dp[total] += dp.get(total - n, 0)

        return dp[target]
        # neetcode -----

s = Solution()
print(s.combinationSum4([2, 3, 6, 7], 7))
print(s.combinationSum4([2, 3], 5))
print(s.combinationSum4([7, 14], 300))
print(s.combinationSum4([2, 3, 6, 10], 15))

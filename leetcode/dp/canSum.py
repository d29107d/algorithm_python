from typing import List


class Solution:
    def canSum(self, candidates: List[int], target: int) -> bool:
        # tabulation -------
        table = {0: True}
        for i in range(target):
            if i in table:
                for candidate in candidates:
                    table[i + candidate] = True

        return table[target] if target in table else False
        # tabulation -------

        # memoization -------
        # memo = {}
        #
        # def helper(helper_target: int) -> bool:
        #     if helper_target in memo:
        #         return memo[helper_target]
        #     if helper_target == 0:
        #         return True
        #     if helper_target < 0:
        #         return False
        #
        #     for candidate in candidates:
        #         remainder = helper_target - candidate
        #         if helper(remainder):
        #             memo[helper_target] = True
        #             return True
        #
        #     memo[helper_target] = False
        #     return False
        #
        # return helper(target)
        # memoization -------


s = Solution()
print(s.canSum([2, 3, 6, 7], 7))
print(s.canSum([2, 3], 7))
print(s.canSum([2, 3, 5], 1))
print(s.canSum([7, 14], 300))

from typing import List


class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        # ret = []
        # memo = {}
        # def helper(start, flag, total):
        #     if start == len(nums):
        #         ret.append(total)
        #         return
        #
        #     key = (start, flag)
        #     if key in memo:
        #         return
        #
        #     num = nums[start]
        #     if flag:
        #         helper(start + 1, True, total)
        #         helper(start + 1, False, total - num)
        #     else:
        #         helper(start + 1, True, total + num)
        #         helper(start + 1, False, total)
        #
        # helper(0, False, 0)
        # return max(ret)

        memo = {}
        def helper(start, flag):
            if start == len(nums):
                return 0

            key = (start, flag)
            if key in memo:
                return memo[key]

            total = nums[start] if flag else -nums[start]
            memo[key] = max(total + helper(start + 1, not flag), helper(start + 1, flag))
            return memo[key]

        return helper(0, True)

        # first, second = 0, 0
        # for i in range(len(nums)):
        #     n = nums[i]
        #     first = max(first, second+n)
        #     second = max(second, first-n)
        #
        # return first

s = Solution()
print(s.maxAlternatingSum([4, 2, 5, 3]))
print(s.maxAlternatingSum([5,6,7,8]))
print(s.maxAlternatingSum([6,2,1,2,4,5]))
# print(s.maxAlternatingSum([4, 2]))

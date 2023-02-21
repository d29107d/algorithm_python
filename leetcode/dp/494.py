from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        count = {0: 1}
        for num in nums:
            tempcount = {}
            for key in count:
                tempcount[key - num] = tempcount.get(key - num, 0) + count[key]
                tempcount[key + num] = tempcount.get(key + num, 0) + count[key]
            count = tempcount
        return count.get(target, 0)

        # def helper(i, total, memo={}):
        #     key = (i, total)
        #     if key in memo:
        #         return memo[key]
        #
        #     if i == len(nums):
        #         return 1 if total == target else 0
        #
        #     n = nums[i]
        #     positive = helper(i + 1, total + n, memo)
        #     negative = helper(i + 1, total - n, memo)
        #     memo[key] = positive + negative
        #     return memo[key]
        #
        # return helper(0, 0)


s = Solution()
print(s.findTargetSumWays([1, 1, 1, 1, 1], 3))
# print(s.findTargetSumWays([9,28,50,9,34,48,2,50,38,10,5,16,44,5,48,21,38,17,21,49], 20))

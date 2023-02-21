from typing import List


class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        first, second = 0, 0
        for i in range(len(nums)):
            n = nums[i]
            first = max(first, second+n)
            second = max(second, first-n)

        return first

s = Solution()
print(s.maxAlternatingSum([4, 2, 5, 3]))
# print(s.maxAlternatingSum([4, 2]))

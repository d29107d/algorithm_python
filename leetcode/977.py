# Given an integer array nums sorted in non-decreasing order,
# return an array of the squares of each number sorted in non-decreasing order.

class Solution:
    def sortedSquares(self, nums):
        l = len(nums) - 1
        result = [0] * (l + 1)
        start,end,r = 0,l,l
        while start <= end:
            s = nums[start] * nums[start]
            e = nums[end] * nums[end]
            if s < e:
                result[r] = e
                end -= 1
            else:
                result[r] = s
                start += 1
            r -= 1
        return result

s = Solution()
print(s.sortedSquares([-4,-1,0,3,10]))
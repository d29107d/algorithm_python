# Given a sorted array of distinct integers and a target value, return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.
#
# You must write an algorithm with O(log n) runtime complexity.

class Solution:
    def searchInsert(self, nums, target: int) -> int:
        if target <= nums[0]:
            return 0

        l = len(nums)
        if target > nums[-1]:
            return l

        start, end = 0, l - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                return mid

        return start

s = Solution()
print(s.searchInsert([1,3,5,6], 2))
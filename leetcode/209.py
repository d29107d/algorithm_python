class Solution:
    def minSubArrayLen(self, target: int, nums) -> int:
        res = float("inf")
        p = 0
        s = 0
        for i,n in enumerate(nums):
            s += n
            while s >= target:
                res = min(res, i - p + 1)
                s -= nums[p]
                p += 1

        return 0 if res == float("inf") else res

s = Solution()
print(s.minSubArrayLen(7, [2,3,1,2,4,3]))
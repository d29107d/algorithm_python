from typing import List


def dfs(nums):
    total, nums_len = sum(nums), len(nums)
    if total % 2 != 0:
        return False

    memo = {}
    half = total // 2

    def helper(cur, target):
        if cur >= nums_len:
            return target == half

        key = (cur, target)
        if key in memo:
            return memo[key]

        # add or skip, here is a tree
        memo[key] = helper(cur + 1, target + nums[cur]) or helper(cur + 1, target)
        return memo[key]

    return helper(0, 0)


def dp_tabulation(nums):
    total, nums_len = sum(nums), len(nums)
    if total % 2 != 0:
        return False

    half = total // 2
    table = [False] * (half + 1)
    table[0] = True

    for num in nums:
        for i in range(half, num - 1, -1):
            if table[half]:
                return True
            table[i] = table[i] or table[i - num]

    return table[half]


def dp_memo(nums):
    total, nums_len = sum(nums), len(nums)
    if total % 2 != 0:
        return False

    half = total // 2
    memo = {}

    def helper(target):
        if target in memo:
            return memo[target]

        if target == half:
            memo[target] = True
            return True

        if target > half:
            memo[target] = False
            return False

        for n in nums:
            if helper(n + target):
                memo[target] = True
                return True

        memo[target] = False
        return False

    return helper(0)


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # return dfs(nums)
        return dp_tabulation(nums)
        # return dp_memo(nums)


print(Solution().canPartition([1, 2, 5]))
print(Solution().canPartition([1, 5, 11, 5]))
print(Solution().canPartition([1, 2, 3, 5]))
print(Solution().canPartition([3, 3, 5]))
print(Solution().canPartition([3, 3]))

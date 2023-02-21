from typing import List


class Solution:
    def wordBreak(self, candidates: List[str], target: str) -> bool:
        memo = {}

        def helper(remainder):
            if remainder in memo:
                return memo[remainder]

            if remainder == '':
                return True

            for candidate in candidates:
                if remainder.find(candidate) == 0:
                    if helper(remainder[len(candidate):]):
                        memo[remainder] = True
                        return True

            memo[remainder] = False
            return False

        return helper(target)


s = Solution()
print(s.wordBreak(["leet", "code"], "leetcode"))
print(s.wordBreak(["apple", "pen"], "applepenapple"))
print(s.wordBreak(["cats", "dog", "sand", "and", "cat"], "catsandog"))
print(s.wordBreak(["car", "ca", "rs"], "cars"))

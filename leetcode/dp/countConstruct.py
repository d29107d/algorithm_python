from typing import List


class Solution:
    def countConstruct(self, candidates: List[str], target: str) -> int:
        memo = {}

        def helper(remainder):
            if remainder in memo:
                return memo[remainder]

            if remainder == '':
                return 1

            total = 0
            for candidate in candidates:
                if remainder.find(candidate) == 0:
                    candidate_len = len(candidate)
                    rest = helper(remainder[candidate_len:])
                    total += rest
                    memo[remainder] = total

            memo[remainder] = total
            return total

        tmp = helper(target)
        return tmp

s = Solution()
# print(s.countConstruct(["leet", "code"], "leetcode"))
# print(s.countConstruct(["apple", "pen"], "applepenapple"))
# print(s.countConstruct(["cats", "dog", "sand", "and", "cat"], "catsandog"))
# print(s.countConstruct(["car", "ca", "rs"], "cars"))
# print(s.countConstruct(['purp', 'p', 'ur', 'le', 'purpi'], "purple"))
print(s.countConstruct(['a', 'ab', 'abc', 'ca', 'bc'], "abcabc"))

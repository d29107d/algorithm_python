from typing import List
from collections import defaultdict


class Solution:
    def countConstruct(self, candidates: List[str], target: str) -> int:
        # dp
        memo = {}
        def dp(remainder):
            if remainder in memo:
                return memo[remainder]

            if remainder == '':
                return 1

            total = 0
            for candidate in candidates:
                if remainder.find(candidate) == 0:
                    candidate_len = len(candidate)
                    rest = dp(remainder[candidate_len:])
                    total += rest
                    memo[remainder] = total

            memo[remainder] = total
            return total

        # tmp = dp(target)

        def tabulation():
            table = defaultdict(int)
            table[0] = 1
            target_len = len(target)

            for i in range(target_len):
                if i in table:
                    for word in candidates:
                        word_len = len(word)
                        end = i + word_len
                        if word == target[i:end]:
                            table[end] += table[i]

            return table[target_len] if target_len in table else 0

        tmp = tabulation()
        return tmp

s = Solution()
print(s.countConstruct(["leet", "code"], "leetcode"))
print(s.countConstruct(["apple", "pen"], "applepenapple"))
print(s.countConstruct(["cats", "dog", "sand", "and", "cat"], "catsandog"))
print(s.countConstruct(["car", "ca", "rs"], "cars"))
print(s.countConstruct(['purp', 'p', 'ur', 'le', 'purpi'], "purple"))
print(s.countConstruct(['a', 'ab', 'abc', 'ca', 'bc'], "abcabc"))

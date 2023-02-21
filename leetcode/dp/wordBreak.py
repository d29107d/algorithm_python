from typing import List


class Solution:
    def wordBreak(self, candidates: List[str], target: str) -> bool:
        # tabulation
        def tabulation():
            table = {0: True}
            target_len = len(target)

            for i in range(target_len):
                if i in table:
                    for word in candidates:
                        word_len = len(word)
                        end = i + word_len
                        if word == target[i:end]:
                            table[end] = True

            return target_len in table

        # dp
        memo = {}

        def dp(remainder):
            if remainder in memo:
                return memo[remainder]

            if remainder == '':
                return True

            for candidate in candidates:
                if remainder.find(candidate) == 0:
                    if dp(remainder[len(candidate):]):
                        memo[remainder] = True
                        return True

            memo[remainder] = False
            return False

        # return dp(target)
        return tabulation()


s = Solution()
print(s.wordBreak(["leet", "code"], "leetcode"))
print(s.wordBreak(["apple", "pen"], "applepenapple"))
print(s.wordBreak(["cats", "dog", "sand", "and", "cat"], "catsandog"))
print(s.wordBreak(["car", "ca", "rs"], "cars"))
print(s.wordBreak(['a', 'ab', 'abc', 'ca', 'bc'], "abcabc"))
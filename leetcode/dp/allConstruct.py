from typing import List


def helper(word_bank, target, memo={}):
    if target in memo:
        return memo[target]

    if target == '':
        return [[]]

    result = []

    for word in word_bank:
        if target.find(word) == 0:
            suffix_ways = helper(word_bank, target[len(word):], memo)
            for way in suffix_ways:
                result.append([word] + way)

    memo[target] = result
    return result


class Solution:
    def allConstruct(self, candidates: List[str], target: str) -> List[List[str]]:
        return helper(candidates, target)


s = Solution()
# print(s.allConstruct(["leet", "code"], "leetcode"))
# print(s.allConstruct(["apple", "pen"], "applepenapple"))
# print(s.allConstruct(["cats", "dog", "sand", "and", "cat"], "catsandog"))
# print(s.allConstruct(["car", "ca", "rs", "s"], "cars"))
# print(s.allConstruct(['purp', 'p', 'ur', 'le', 'purpi'], "purple"))
print(s.allConstruct(['a', 'ab', 'abc', 'ca', 'bc'], "abcabc"))
print(s.allConstruct(['abc', 'ab', 'ca', 'bc'], ""))

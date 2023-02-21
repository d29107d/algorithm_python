from typing import List
from collections import defaultdict


def dp(word_bank, target, memo={}):
    if target in memo:
        return memo[target]

    if target == '':
        return [[]]

    result = []

    for word in word_bank:
        if target.find(word) == 0:
            suffix_ways = dp(word_bank, target[len(word):], memo)
            for way in suffix_ways:
                result.append([word] + way)

    memo[target] = result
    return result


def tabulation(candidates: List[str], target: str):
    target_len = len(target)
    table = {k: None for k in range(target_len)}
    table[0] = []

    for i in range(target_len):
        if table[i] is not None:
            for word in candidates:
                end = i + len(word)
                if word == target[i:end]:
                    if end not in table or table[end] is None:
                        table[end] = []

                    if not table[i]:
                        table[end].append([word])
                    else:
                        for j in range(len(table[i])):
                            tmp = table[i][j] + [word]
                            table[end].append(tmp)

    return table[target_len] if target_len in table else [[]]

class Solution:
    def allConstruct(self, candidates: List[str], target: str) -> List[List[str]]:
        # return dp(candidates, target)
        return tabulation(candidates, target)

s = Solution()
print(s.allConstruct(["leet", "code"], "leetcode"))
print(s.allConstruct(["apple", "pen"], "applepenapple"))
print(s.allConstruct(["cats", "dog", "sand", "and", "cat"], "catsandog"))
print(s.allConstruct(["car", "ca", "rs", "s"], "cars"))
print(s.allConstruct(['purp', 'p', 'ur', 'le', 'purpi'], "purple"))
print(s.allConstruct(['a', 'ab', 'abc', 'ca', 'bc'], "abcabc"))
print(s.allConstruct(['abc', 'ab', 'ca', 'bc'], ""))

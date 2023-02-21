from typing import List


class Solution:
    # def bestSum_dp(self, candidates: List[int], target: int) -> List[int]:
    #     def dp(remainder, memo={}):
    #         if remainder in memo:
    #             return memo[remainder]
    #
    #         if remainder <= 0:
    #             return []
    #
    #         shortestCombination = []
    #         for num in candidates:
    #             rem = remainder - num
    #             remCombination = dp(rem, memo)
    #             if remCombination:
    #                 combination = remCombination + [num]
    #                 if not shortestCombination or len(combination) < len(shortestCombination):
    #                     shortestCombination = combination
    #
    #         memo[remainder] = shortestCombination
    #         return shortestCombination
    #
    #     return dp(target)

    def bestSum_dfs(self, candidates: List[int], target: int) -> List[int]:
        if target <= 0:
            return []

        res = {'data': []}

        def dfs(start, path):
            total = sum(path)

            if start >= len(candidates) or len(candidates) == 0 or total > target:
                return

            if res['data'] != [] and len(path) >= len(res['data']):
                return

            if total == target:
                if (res['data'] != [] and len(path) < len(res['data'])) or res['data'] == []:
                    res['data'] = path
                return

            dfs(start, path + [candidates[start]])
            dfs(start + 1, path)
            # dfs(start, path + [candidates[start]])

        dfs(0, [])
        return res['data']


s = Solution()
print(s.bestSum_dfs([2, 3], 4))
print(s.bestSum_dfs([10, 6, 2, 3, 15], 15))
print(s.bestSum_dfs([7, 14, 15], 300))

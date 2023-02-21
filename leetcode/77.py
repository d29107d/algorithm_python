from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # self ------
        # ret = {i: [] for i in range(1, 1 + k)}
        # # ret[0] = [[i] for i in range(1, n + 1)]
        # ret[0] = [[]]
        # memo = {}
        #
        # def helper(cur, i):
        #     if cur > k:
        #         return
        #     for num in range(i, n + 1):
        #         for r in ret[cur - 1]:
        #             tmp = [num] + r
        #             key = tuple(set(tmp))
        #             if num in r or key in memo:
        #                 continue
        #             memo[key] = True
        #             ret[cur].append(tmp)
        #     helper(cur + 1, i + 1)
        #
        # helper(1, 1)
        # return ret[k]
        # self ------

        # dfs -------
        ret = []

        def dfs(start, path):
            if len(path) == k:
                ret.append(path)
                return

            for i in range(start, n + 1):
                dfs(i + 1, path + [i])
        dfs(1, [])
        return ret
        # dfs -------


print(Solution().combine(4, 2))

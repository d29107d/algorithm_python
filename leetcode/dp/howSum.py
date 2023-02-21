from typing import List


class Solution:
    def how_sum(self, numbers: List[int], target: int) -> List[int]:
        table = {0: []}

        for i in range(target + 1):
            if i in table:
                for num in numbers:
                    table[i + num] = table[i] + [num]

        return table[target] if target in table else None


s = Solution()
print(s.how_sum([2, 3], 7))
print(s.how_sum([2, 4], 7))
print(s.how_sum([10, 6, 2, 3, 15], 15))
print(s.how_sum([7, 14], 300))

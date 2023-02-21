class Solution:
    def fib(self, n: int) -> int:
        table = [0 for _ in range(n + 1)]
        table[1] = 1
        for i in range(2, n + 1):
            table[i] += (table[i - 2] + table[i - 1])

        return table[n]


s = Solution()
print(s.fib(6))
print(s.fib(7))
print(s.fib(8))
print(s.fib(50))

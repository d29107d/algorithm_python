# Given a matrix of shape N×N arranged in a "spiral", with its numbers spiralling from 1 to N² inward,
# what is the sum of its diagonals? See examples to clarify what a spiral is.
#
# Example 1:
# The input: 3
# Gives the following spiral:
# 1     2     3
# 8     9     4
# 7     6     5
# The sum of the diagonals is:
# 1 + 3 + 5 + 7 + 9 = 25
#
#
# Example 2:
# The input: 4
# Gives the following spiral:
# 1    2      3     4
# 12   13    14     5
# 11   16    15     6
# 10   9      8     7
# The sum of the diagonals is:
# 1 + 4 + 7 + 10 + 13 + 14 + 15 + 16 = 80

n = 1453

m = n * n
i = 1
step = n - 1
s = i
c = 0
while i < m:
    if c % 4 == 0 and c > 1:
        step -= 2
    i += step
    s += i
    if step < 0:
        break
    c += 1

print(s)
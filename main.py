import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
s=int(math.sqrt(n))
m=int(n/s)
print(m, file=sys.stderr, flush=True)
print(n,s, file=sys.stderr, flush=True)
while n % m != 0:
    m-=1
print(m, file=sys.stderr, flush=True)

a,b=sorted([int(n/m), m])
print(str(a)+'*'+str(b))
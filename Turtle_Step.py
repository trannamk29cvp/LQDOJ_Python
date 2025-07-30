# https://lqdoj.edu.vn/problem/gcdinc2seq
import sys
x, k = map(int, input().split())
if k == 0:
    print(x)
    sys.exit(0)
if x % 2 == 0:
    print(2)
else:
    print(1)

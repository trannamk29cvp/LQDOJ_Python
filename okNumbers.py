# https://lqdoj.edu.vn/problem/oknumbers
# import sys
# sys.stdin = open("tenbai.inp", "r")
# sys.stdout = open("tenbai.out", "w")

l, r = map(int, input().split())
mod = int(1e9 + 7)
okNum = 1
for i in range(2, l+1):
    okNum = (okNum * 10 + 1) % mod

total = okNum
for i in range(l+1, r+1):
    okNum = (okNum * 10 + 1) % mod
    total = (total + okNum) % mod
print(int(total % mod))

# https://lqdoj.edu.vn/problem/cses1090
n, x = map(int, input().split())
p = list(map(int, input().split()))
p.sort()
i, j = 0, n-1
gon = 0
while i <= j:
    if p[i] + p[j] <= x and i != j:
        gon += 1
        i += 1
        j -= 1
    else:
        gon += 1
        j -= 1
print(gon)

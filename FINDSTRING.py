# https://lqdoj.edu.vn/problem/cdl5p6
s = input()
q = int(input())
for i in range(q):
    x = input()
    ok = False
    for j in range(0, len(s) - len(x) + 1):
        if x == s[j:len(x)+j]:
            print(j)
            ok = True
            break
    if not ok:
        print(-1)

import sys

n, m = map(int, sys.stdin.readline().split())
a, b = [0], [0]

for _ in range(n):
    v, t = map(int, sys.stdin.readline().split())
    for i in range(t):
        a.append(a[-1] + v)

for _ in range(m):
    v, t = map(int, sys.stdin.readline().split())
    for i in range(t):
        b.append(b[-1] + v)


res = -1
pre = -1

for i in range(len(a)):
    if a[i] > b[i] and pre != 0:
        pre = 0
        res += 1
    elif a[i] < b[i] and pre != 1:
        pre = 1
        res+=1
print(res)
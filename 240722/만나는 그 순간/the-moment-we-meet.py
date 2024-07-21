import sys

N, M = map(int, sys.stdin.readline().split())
a, b = [0], [0]

for _ in range(N):
    d, t = map(str, sys.stdin.readline().split())

    for i in range(int(t)):
        if d == "L":
            a.append(a[-1] - 1)
        else:
            a.append(a[-1] + 1)

for _ in range(M):
    d, t = map(str, sys.stdin.readline().split())

    for i in range(int(t)):
        if d == "L":
            b.append(b[-1] - 1)
        else:
            b.append(b[-1] + 1)

for i in range(1,len(a)):
    if a[i] == b[i]:
        print(i)
        exit()
print("-1")
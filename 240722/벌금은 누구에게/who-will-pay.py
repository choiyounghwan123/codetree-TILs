import sys

n,m,k = map(int,sys.stdin.readline().split())
b = [0] * (n+1)

for _ in range(m):
    a = int(sys.stdin.readline())
    b[a] += 1
    if b[a] == k:
        print(a)
        exit()


print("-1")
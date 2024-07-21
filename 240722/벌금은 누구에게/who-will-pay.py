import sys

n,m,k = map(int,sys.stdin.readline().split())
b = [0] * (n+1)

for _ in range(m):
    b[int(sys.stdin.readline())] += 1

for i in range(n+1):
    if b[i] == k:
        print(i)
        exit()

print("-1")
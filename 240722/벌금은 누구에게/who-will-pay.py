import sys

n,m,k = map(int,sys.stdin.readline().split())
penalty = [0] * (n+1)

for _ in range(m):
    a = int(sys.stdin.readline())
    penalty[a] += 1
    if penalty[a] == k:
        print(a)
        exit()


print("-1")
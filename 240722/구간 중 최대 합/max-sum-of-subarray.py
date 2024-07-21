import sys

n, k = map(int, sys.stdin.readline().split())
nums: list = list(map(int, sys.stdin.readline().split()))

res:int = -1

for i in range(n-k+1):
    temp:int = 0
    for j in range(i,i+3):
        temp += nums[j]
    res = max(res,temp)
print(res)
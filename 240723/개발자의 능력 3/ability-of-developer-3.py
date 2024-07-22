# 개발자의 능력 3

import sys

nums = list(map(int, sys.stdin.readline().split()))


def get_diff(i, j, k):
    sum1 = nums[i] + nums[j] + nums[k]
    sum2 = sum(nums) - sum1
    return abs(sum1 - sum2)

min_diff = sys.maxsize

for i in range(6):
    for j in range(i+1,6):
        for k in range(j+1,6):
            min_diff = min(get_diff(i,j,k),min_diff)

print(min_diff)
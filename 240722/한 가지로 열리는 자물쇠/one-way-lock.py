# 한 가지로 열리는 자물쇠

import sys

N:int = int(sys.stdin.readline())
a, b, c = map(int, sys.stdin.readline().split())

res: int = 0

for i in range(1, N + 1):
    for j in range(1, N + 1):
        for k in range(1, N + 1):
            if a - 2 <= i <= a + 2 or b - 2 <= j <= b + 2 or c - 2 <= k <= c + 2:
                res += 1

print(res)
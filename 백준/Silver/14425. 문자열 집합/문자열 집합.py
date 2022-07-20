import sys

n, m = map(int, sys.stdin.readline().split())
cnt = 0
S = {}

for i in range(n):
    index = sys.stdin.readline().strip()
    S[index] = True

for j in range(m):
    check = sys.stdin.readline().strip()
    if check in S:
        cnt += 1
print(cnt)
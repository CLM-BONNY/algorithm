import sys

# 입력 받기
n = int(sys.stdin.readline().strip())
a = list(map(int, sys.stdin.readline().strip().split()))

# DP 테이블 생성하기 - 가장 긴 증가하는 부분 수열
dp = [1] * n

# 가장 긴 증가하는 부분 수열 계산하기
for i in range(1, n):
    for j in range(i):
        if a[i] > a[j]:
            dp[i] = max(dp[i], dp[j] + 1)

# 결과 출력
print(max(dp))

import sys
import math

# 입력 받기
m, n = map(int, sys.stdin.readline().strip().split())

# 소수 판별을 위한 배열 초기화
is_prime = [True] * (n + 1)
is_prime[0] = is_prime[1] = False  # 0과 1은 소수가 아님

# 에라토스테네스의 체 알고리즘
for i in range(2, int(math.sqrt(n)) + 1):
    if is_prime[i]:
        for j in range(i * i, n + 1, i):
            is_prime[j] = False

# M 이상 N 이하의 소수 출력
for i in range(m, n + 1):
    if is_prime[i]:
        print(i)
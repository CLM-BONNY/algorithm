import sys
from collections import Counter

# 입력 받기
n = int(sys.stdin.readline().strip())

num = [int(sys.stdin.readline().strip()) for _ in range(n)]

# 산술 평균
print(round(sum(num) / n))

# 중앙값
num.sort()
print(num[n//2])

# 최빈값
counter = Counter(num)
max_freq = max(counter.values())

# 최빈값 중에서 빈도수가 같은 값들을 찾고, 그 중 두 번째로 작은 값을 선택
modes = [key for key, value in counter.items() if value == max_freq]
modes.sort()

if len(modes) > 1:
    print(modes[1])
else:
    print(modes[0])


# 범위
print(max(num) - min(num))
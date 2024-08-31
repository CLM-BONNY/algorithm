import sys

# 입력 받기
n = int(sys.stdin.readline().strip())

sizes = list(map(int, sys.stdin.readline().strip().split()))

t, p = map(int, sys.stdin.readline().strip().split())

# 티셔츠 계산
dress = 0
for x in sizes:
  if x % t == 0:
    dress += x // t
  else:
    dress += x // t + 1

print(dress)

# 펜 계산
print(n // p, n % p)
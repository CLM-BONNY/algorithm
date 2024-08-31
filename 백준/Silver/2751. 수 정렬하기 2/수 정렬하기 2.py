import sys

# 입력 받기
n = int(sys.stdin.readline().strip())

num = [int(sys.stdin.readline().strip()) for _ in range(n)]

# 정렬하기
num.sort()

# 출력하기
for i in num:
  print(i)
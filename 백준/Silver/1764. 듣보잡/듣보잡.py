import sys
from collections import Counter

# 입력 받기
a, b = map(int, sys.stdin.readline().strip().split())

name = []

# 듣도 못한 사람 입력 받기
for i in range(a):
  name.append(sys.stdin.readline().strip())

# 보도 못한 사람 입력 받기
for j in range(b):
  name.append(sys.stdin.readline().strip())

# 이름 등장 횟수 계산
name_count = Counter(name)

# 2번 등장한 이름만 남기기
name = [name for name, count in name_count.items() if count == 2]

name.sort()

# 결과 출력하기
print(len(name))
for n in name:
  print(n)

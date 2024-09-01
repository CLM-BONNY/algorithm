import sys

# 입력 받기
n = int(sys.stdin.readline().strip())

num = list(map(int, sys.stdin.readline().strip().split()))

m = int(sys.stdin.readline().strip())

targets = list(map(int, sys.stdin.readline().strip().split()))

# 탐색 대상 배열 정렬
num.sort()

#  이분 탐색 진행 및 결과 출력
for target in targets:
  left, right = 0, n-1
  found = False
  
  while left <= right:
    mid = (left + right) // 2
    if num[mid] == target:
      print(1)
      found = True
      break
    elif num[mid] < target:
      left = mid + 1
    else:
      right = mid - 1
  
  if not found:
    print(0)

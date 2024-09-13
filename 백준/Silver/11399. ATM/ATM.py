import sys

# 입력 받기
N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

# 오름차순 정렬하기
nums.sort()

# 인출에 필요한 시간 최솟값 계산하기
time_sum, final_time = 0, 0

for number in nums:
  time_sum += number
  final_time += time_sum
  
# 결과 출력하기
print(final_time)
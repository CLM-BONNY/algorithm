# 입력 받기
N = int(input())
ropes = [int(input()) for _ in range(N)]

# 로프 길이 오름차순 정렬
ropes.sort(reverse=True)

max_weight = 0

# 각 로프에 대해 최대 중량 계산
for i in range(N):
  current_weight = ropes[i] * (i + 1)
  max_weight = max(max_weight, current_weight)

print(max_weight)
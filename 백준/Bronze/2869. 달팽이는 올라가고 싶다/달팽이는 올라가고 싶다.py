import math

# 입력 받기
A, B, V = map(int, input().split())

# 정상까지 도달하기 전까지 필요한 이동 거리
distance_to_climb = V - A

# 하루 이동 거리
daily_climb = A - B

# 필요한 날수 계산
days = math.ceil(distance_to_climb / daily_climb) + 1

# 결과 출력
print(days)

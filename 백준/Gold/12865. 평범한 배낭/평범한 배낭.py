# 입력받기
N, K = map(int, input().split())

# 물건 정보 입력받기
items = [list(map(int, input().split())) for _ in range(N)]

# DP 테이블 초기화 (행: 물건, 열: 무게)
dp = [[0] * (K + 1) for _ in range(N + 1)]

# DP로 최대 가치 계산
for i in range(1, N + 1):
    weight, value = items[i - 1]
    for j in range(1, K + 1):
        # 현재 물건을 가방에 넣을 수 있는 경우
        if weight <= j:
            # 물건을 넣었을 때와 넣지 않았을 때 중 최대 가치 선택
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight] + value)
        else:
            # 물건을 가방에 넣을 수 없는 경우 이전 상태 그대로 유지
            dp[i][j] = dp[i - 1][j]

# 출력하기
print(dp[N][K])

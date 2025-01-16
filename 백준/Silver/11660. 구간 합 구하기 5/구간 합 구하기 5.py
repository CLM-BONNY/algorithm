import sys
input = sys.stdin.readline

# 입력 받기
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 2차원 누적 합을 저장할 배열 (1-based index 사용)
prefix_sum = [[0] * (N + 1) for _ in range(N + 1)]

# 누적 합 계산
for i in range(1, N + 1):
    for j in range(1, N + 1):
        prefix_sum[i][j] = prefix_sum[i - 1][j] + prefix_sum[i][j - 1] \
                           - prefix_sum[i - 1][j - 1] + arr[i - 1][j - 1]

# M개의 쿼리를 처리
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    result = prefix_sum[x2][y2] - prefix_sum[x2][y1 - 1] \
             - prefix_sum[x1 - 1][y2] + prefix_sum[x1 - 1][y1 - 1]
    print(result)

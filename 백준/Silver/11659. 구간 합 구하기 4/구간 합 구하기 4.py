import sys

# 입력 받기
data = sys.stdin.read().split()

# 첫 번째 줄: N, M
N, M = map(int, data[:2])

# 두 번째 줄: N개의 수
numbers = list(map(int, data[2:2 + N]))

# 누적 합 배열 계산
prefix_sum = [0] * (N + 1)
for i in range(1, N + 1):
    prefix_sum[i] = prefix_sum[i - 1] + numbers[i - 1]

# 구간 합 계산
output = []
query_start_index = 2 + N
for k in range(M):
    i, j = map(int, data[query_start_index + 2 * k: query_start_index + 2 * k + 2])
    output.append(prefix_sum[j] - prefix_sum[i - 1])

# 결과 출력
print("\n".join(map(str, output)) + "\n")

import sys

def solve(N):
    # 첫 줄 입력을 먼저 받고, 초기값 설정
    max_dp = list(map(int, sys.stdin.readline().split()))
    min_dp = max_dp[:]

    for _ in range(N - 1):
        cur = list(map(int, sys.stdin.readline().split()))

        # 최대값 갱신
        new_max = [
            cur[0] + max(max_dp[0], max_dp[1]),
            cur[1] + max(max_dp[0], max_dp[1], max_dp[2]),
            cur[2] + max(max_dp[1], max_dp[2])
        ]
        
        # 최소값 갱신
        new_min = [
            cur[0] + min(min_dp[0], min_dp[1]),
            cur[1] + min(min_dp[0], min_dp[1], min_dp[2]),
            cur[2] + min(min_dp[1], min_dp[2])
        ]

        # 현재 DP 값을 새로운 값으로 업데이트
        max_dp = new_max
        min_dp = new_min

    return max(max_dp), min(min_dp)


# 입력 받기
N = int(sys.stdin.readline().strip())

# 결과 출력하기
max_score, min_score = solve(N)
print(max_score, min_score)

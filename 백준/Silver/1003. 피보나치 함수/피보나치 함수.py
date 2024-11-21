def fibonacci_count(n):
    # DP 배열 초기화
    dp = [[0, 0] for _ in range(n + 1)]
    dp[0] = [1, 0]  # fibonacci(0): 0 한 번 출력
    if n > 0:
        dp[1] = [0, 1]  # fibonacci(1): 1 한 번 출력
    
    # DP 점화식 계산
    for i in range(2, n + 1):
        dp[i][0] = dp[i - 1][0] + dp[i - 2][0]
        dp[i][1] = dp[i - 1][1] + dp[i - 2][1]
    
    return dp[n]

# 입력 받기
t = int(input())  # 테스트 케이스 개수
results = []

for _ in range(t):
    n = int(input())
    results.append(fibonacci_count(n))

# 결과 출력
for result in results:
    print(result[0], result[1])

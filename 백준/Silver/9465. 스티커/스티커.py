def max_sticker_score(n, stickers):
    # 스티커가 1개일 경우 예외 처리
    if n == 1:
        return max(stickers[0][0], stickers[1][0])

    # DP 테이블 초기화 
    dp = [[0] * n for _ in range(2)]
    dp[0][0] = stickers[0][0]
    dp[1][0] = stickers[1][0]
    dp[0][1] = stickers[1][0] + stickers[0][1]
    dp[1][1] = stickers[0][0] + stickers[1][1]

    # 각 열마다 최대 점수 계산
    for i in range(2, n):
        dp[0][i] = max(dp[1][i-1], dp[1][i-2]) + stickers[0][i]
        dp[1][i] = max(dp[0][i-1], dp[0][i-2]) + stickers[1][i]

    # 최종 최대 점수 반환
    return max(dp[0][n-1], dp[1][n-1])

# 입력 및 처리
T = int(input())
for _ in range(T):
    n = int(input())
    stickers = [list(map(int, input().split())) for _ in range(2)]
    print(max_sticker_score(n, stickers))

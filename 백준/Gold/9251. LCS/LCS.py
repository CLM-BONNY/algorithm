import sys

def lcs(str1, str2):
    len1, len2 = len(str1), len(str2)
    
    # DP 테이블 초기화 (0으로 채운 (len1+1) x (len2+1) 2D 배열)
    dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]

    # LCS DP 테이블 채우기
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if str1[i - 1] == str2[j - 1]:  # 같은 문자일 경우
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:  # 다른 문자일 경우
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[len1][len2]

# 입력 받기
str1 = sys.stdin.readline().strip()
str2 = sys.stdin.readline().strip()

# 결과 출력하기
print(lcs(str1, str2))

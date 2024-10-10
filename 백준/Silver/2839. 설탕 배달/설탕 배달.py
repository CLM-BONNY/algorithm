# 입력 받기 
N = int(input())

bags = -1  # 기본값은 -1로 설정(결과가 없을 경우 -1 출력)
for i in range(N // 5, -1, -1):  # N을 5로 나눈 몫에서 0까지 감소시키며 반복
    remaining = N - (i * 5)  # 5킬로그램 봉지를 사용한 후 남은 설탕
    if remaining % 3 == 0:  # 남은 설탕이 3으로 나눠지면
        bags = i + (remaining // 3)  # 5킬로그램 봉지 개수 + 3킬로그램 봉지 개수
        break  # 반복 종료

print(bags)

def padovan_sequence(max_n):
    # 파도반 수열을 저장할 리스트 초기화
    padovan = [0] * (max_n + 1)
    # 초기값 설정
    padovan[1] = padovan[2] = padovan[3] = 1
    
    # 점화식을 이용해 수열 계산
    for i in range(4, max_n + 1):
        padovan[i] = padovan[i - 2] + padovan[i - 3]
    
    return padovan

# 입력 받기
t = int(input())
cases = [int(input()) for _ in range(t)]
max_n = max(cases)

# 파도반 수열 계산
padovan = padovan_sequence(max_n)

# 출력하기
for n in cases:
    print(padovan[n])

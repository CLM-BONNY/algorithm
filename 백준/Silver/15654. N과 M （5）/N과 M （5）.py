# 가능한 모든 순열 생성 함수
def all_comb(arr, M, result, used, current):
    # 현재 수열의 길이가 M과 같아지면 수열 출력
    if len(current) == M:
        print(' '.join(map(str, current)))
        return
    
    # 배열의 모든 원소에 대해 반복
    for i in range(len(arr)):
        # 아직 사용되지 않은 원소인 경우
        if not used[i]:
            # 해당 원소 사용 표시
            used[i] = True
            # 현재 수열에 원소 추가
            current.append(arr[i])
            
            # 재귀적으로 다음 원소 탐색
            all_comb(arr, M, result, used, current)
            
            # 백트래킹: 상태 원복
            used[i] = False
            current.pop()

# 입력 받기
N, M = map(int, input().split())
arr = list(map(int, input().split()))

# 배열 정렬
arr.sort()  

# 숫자 사용 여부 추적 배열
used = [False] * N

# 결과 저장 리스트
result = []

# 모든 가능한 M 길이의 순열 생성 시작
all_comb(arr, M, result, used, [])

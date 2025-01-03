def dfs(arr, M, current):
    # 수열의 길이가 M이 되면 출력하기
    if len(current) == M:
        print(' '.join(map(str, current)))
        return
    
    # 중복 방지를 위한 변수
    prev = 0
    
    # 현재 수열의 마지막 원소부터 시작
    start = current[-1] if current else 0
    
    for num in arr:
        # 비내림차순 조건 확인
        if not current or num >= current[-1]:
            # 중복 수열 방지
            if num != prev:
                current.append(num)
                dfs(arr, M, current)
                current.pop()
                prev = num

# 입력 받기
N, M = map(int, input().split())

# 정렬하기
numbers = sorted(list(map(int, input().split())))

# DFS 함수 호출하기
dfs(numbers, M, [])

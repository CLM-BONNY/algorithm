def solve(n, m, current_sequence, start):
    # 현재 시퀀스의 길이가 m과 같을 경우, 시퀀스를 출력하고 함수 종료
    if len(current_sequence) == m:
        print(' '.join(map(str, current_sequence)))
        return
    # start부터 n까지 반복하여 각 숫자를 시퀀스에 추가하고 재귀 호출
    for i in range(start, n + 1):
        solve(n, m, current_sequence + [i], i)

# 입력 받기
n, m = map(int, input().split())

# 함수 호출
solve(n, m, [], 1)

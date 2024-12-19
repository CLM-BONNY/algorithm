from collections import deque


def solve(A, B):
    queue = deque([(A, 0)])  # (현재 숫자, 연산 횟수)
    visited = set([A])  # 방문한 숫자를 저장

    while queue:
        current, steps = queue.popleft()

        # 목표 숫자에 도달했을 때
        if current == B:
            return steps + 1

        # 2를 곱하는 연산
        next_num = current * 2
        if next_num <= B and next_num not in visited:
            queue.append((next_num, steps + 1))
            visited.add(next_num)

        # 1을 가장 오른쪽에 추가하는 연산
        next_num = current * 10 + 1
        if next_num <= B and next_num not in visited:
            queue.append((next_num, steps + 1))
            visited.add(next_num)

    # 목표 숫자에 도달하지 못한 경우
    return -1

# 입력 받기
A, B = map(int, input().split())

# 함수 호출 및 결과 출력
result = solve(A, B)
print(result)

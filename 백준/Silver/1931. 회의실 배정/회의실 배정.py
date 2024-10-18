# 입력 받기
n = int(input())  # 회의의 수
meetings = []

for _ in range(n):
    start, end = map(int, input().split())
    meetings.append((start, end))

# 회의 종료 시간을 기준으로 정렬, 끝나는 시간이 같다면 시작 시간 기준으로 정렬
meetings.sort(key=lambda x: (x[1], x[0]))

# 그리디 알고리즘을 통한 회의 선택
count = 0
last_end_time = 0

for start, end in meetings:
    if start >= last_end_time:
        count += 1
        last_end_time = end

# 결과 출력
print(count)
import sys

# 입력 받기
n = int(sys.stdin.readline().strip())

# 1부터 10,000까지의 숫자를 카운팅할 배열 생성
count = [0] * 10001

# 입력된 숫자 카운팅
for _ in range(n):
    num = int(sys.stdin.readline().strip())
    count[num] += 1

# 카운팅된 결과를 바탕으로 오름차순 출력
for i in range(10001):
    if count[i] > 0:
        for _ in range(count[i]):
            print(i)
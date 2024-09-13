import sys
from collections import deque

# 입력 받기
N = int(sys.stdin.readline().strip())

# 카드 초기화하기
queue = deque(range(1, N+1))

# 카드가 한 장 남을 때까지 반복하기
while len(queue) > 1:
  # 제일 위에 있는 카드 버리기
  queue.popleft()
  
  # 제일 위에 있는 카드 제일 아래로 옮기기
  queue.append(queue.popleft())

# 결과 출력하기
print(queue[0])
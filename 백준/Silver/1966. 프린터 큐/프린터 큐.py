from collections import deque

# 입력 받기
test_cases = int(input())

for _ in range(test_cases):
    # 문서의 개수 N, 궁금한 문서의 위치 M 입력
    N, M = map(int, input().split())
    
    # 문서들의 중요도 입력
    importance = list(map(int, input().split()))
    
    # (인덱스, 중요도) 형태로 큐에 저장
    queue = deque((i, importance[i]) for i in range(N))
    
    # 인쇄 순서
    count = 0
    
    while queue:
        # 현재 큐에서 첫 번째 문서를 확인
        current = queue.popleft()
        
        # 나머지 문서 중 현재 문서보다 중요도가 높은 문서가 있는지 확인
        if any(current[1] < doc[1] for doc in queue):
            # 중요도가 더 높은 문서가 있으면 뒤로 보냄
            queue.append(current)
        else:
            # 그렇지 않으면 인쇄
            count += 1
            if current[0] == M:
                # 현재 문서가 우리가 찾는 문서일 경우
                print(count)
                break

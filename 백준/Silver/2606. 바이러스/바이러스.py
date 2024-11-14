# 입력 받기
n = int(input())  # 컴퓨터의 수
m = int(input())  # 네트워크 상에서 연결된 쌍의 수

# 인접 리스트 생성
network = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    network[a].append(b)
    network[b].append(a)

# 방문한 컴퓨터를 체크하기 위한 리스트
visited = [False] * (n + 1)

# DFS 함수 정의
def dfs(v):
    visited[v] = True
    count = 1  # 감염된 컴퓨터 수를 세기 위한 변수
    for i in network[v]:
        if not visited[i]:
            count += dfs(i)
    return count

# 1번 컴퓨터가 감염되었을 때 감염되는 컴퓨터 수 계산
infected_computers = dfs(1) - 1  # 1번 컴퓨터 제외

# 결과 출력하기
print(infected_computers)

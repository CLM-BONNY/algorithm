import sys
import heapq

def dijkstra(n, graph, start, end):
    INF = float('inf')
    distance = [INF] * (n + 1)
    distance[start] = 0
    pq = [(0, start)]  # (비용, 도시)

    while pq:
        cost, now = heapq.heappop(pq)

        if distance[now] < cost:
            continue

        for next_node, next_cost in graph[now]:
            new_cost = cost + next_cost

            if new_cost < distance[next_node]:
                distance[next_node] = new_cost
                heapq.heappush(pq, (new_cost, next_node))

    return distance[end]

# 입력 받기
n = int(sys.stdin.readline().strip())  # 도시 개수
m = int(sys.stdin.readline().strip())  # 버스 개수

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))

start, end = map(int, sys.stdin.readline().split())

# 최단 거리 출력
print(dijkstra(n, graph, start, end))

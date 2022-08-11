def dfs(node, cnt):
    check[node] = 1
    n = graph[node][0]
    if check[n] == 0:
        cnt = dfs(n, cnt+1)
    return cnt

N = int(input())
graph = [[] for _ in range(N+1)]
res = [0]*(N+1)
for u in range(1, N+1):
    v = int(input())
    graph[u].append(v)
for i in range(1, N+1):
    check = [0]*(N+1)
    res[i] = dfs(i, 1)
print(res.index(max(res)))
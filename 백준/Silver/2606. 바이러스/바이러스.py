n = int(input())
v = int(input())

graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for i in range(v):
    a, b = [int(i) for i in input().split()]
    graph[a].append(b)
    graph[b].append(a) # 양방향 연결

def dfs(v):
    visited[v] = 1
    for nextNode in graph[v]:
        if visited[nextNode]==0:
            dfs(nextNode)

dfs(1)
print(sum(visited)-1)
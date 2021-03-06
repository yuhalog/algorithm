# 2606 : 바이러스 - DFS

import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

matrix = [[0]*(n+1) for _ in range(n+1)]
visited = [0 for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    matrix[a][b] = matrix[b][a] = 1


def dfs(v):
    visited[v] = 1

    for i in range(n+1):
        if visited[i] == 0 and matrix[v][i] == 1:
            dfs(i)


dfs(1)
ans = sum(visited)-1
print(ans)

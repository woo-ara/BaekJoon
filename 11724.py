'''
22.09.29 우아라
백준 11724
'''


import sys

sys.setrecursionlimit(10000)


def dfs(v):
    visited[v] = True
    for e in adj[v]:
        if not visited[e]:
            dfs(e)


N, M = map(int, input().split())
adj = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
count = 0

for _ in range(M):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

for j in range(1, N + 1):
    if not visited[j]:
        dfs(j)
        count += 1

print(count)


# # DFS 메서드 정의
# def dfs(graph, v, visited):
#     # 현재 노드를 방문 처리
#     visited[v] = True
#     print(v, end=' ')
#     # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
#     for i in graph[v]:
#         if not visited[i]:
#             dfs(graph, i, visited)
#
# # 각 노드가 연결된 정보를 표현(2차원 리스트)
# graph = [
#     [],
#     [2,3,8], # 1번 노드와 연결
#     [1,7], # 2번 노드와 연결
#     [1,4,5], # ...
#     [3,5],
#     [3,4],
#     [7],
#     [2,6,8],
#     [1,7]
# ]
#
# # 각 노드가 방문된 정보를 표현 (1차원 리스트)
# visited = [False] * 9
#
# # 정의된 DFS 함수 호출
# dfs(graph, 1, visited)
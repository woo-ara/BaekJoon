'''
백준 1926 그림
22.11.18 우아라
'''

'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)

n,m = map(int,input().split())
graph = []
dx = [1,-1,0,0]
dy = [0,0,1,-1]
for _ in range(n):
    graph.append(list(map(int,input().split())))

def dfs(x,y):
    global cnt
    cnt += 1
    graph[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if -1<nx<n and -1<ny<m and graph[nx][ny]==1:
            dfs(nx,ny)

num_list = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            cnt=0
            dfs(i,j)
            num_list.append(cnt)

if len(num_list)==0:
    print(len(num_list))
    print(0)
else:
    print(len(num_list))
    print(max(num_list))
'''

'''
from collections import deque

n, m = map(int, input().split())
graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(graph, a, b):
    queue = deque()
    queue.append((a, b))
    graph[a][b] = 0
    count = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
                count += 1
    return count


paint = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            paint.append(bfs(graph, i, j))

if len(paint) == 0:
    print(len(paint))
    print(0)
else:
    print(len(paint))
    print(max(paint))
'''


'''
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(i, j, graph):
    q = deque([[i, j]])
    graph[i][j] = 0
    count = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 < nx <= n and 0 < ny <= m and graph[nx][ny] == 1:
                q.append([nx, ny])
                graph[nx][ny] = 2
                count += 1
    return count

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

paint = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            paint.append(bfs(i, j, graph))

if len(paint) == 0:
    print(len(paint))
    print(0)
else:
    print(len(paint))
    print(max(paint))
    
'''


import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

count = []
v = [[0] * m for _ in range(n)]

def bfs(i, j):
    global cnt
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque()
    q.append([i, j])
    v[i][j] = 1
    while q:
        x, y = q.popleft()

        for k in range(4):
            nowx, nowy = x + dx[k], y + dy[k]

            if 0 <= nowx < n and 0 <= nowy < m :
                if arr[nowx][nowy] == 1 and v[nowx][nowy] == 0:
                    q.append([nowx, nowy])
                    v[nowx][nowy] = 1
                    cnt += 1
    count.append(cnt)

for i in range(n):
    for j in range(m):
        if(arr[i][j] == 1 and v[i][j] == 0):
            cnt = 1
            bfs(i, j)

if(len(count) == 0):
    print(len(count))
    print(0)
else:
    print(len(count))
    print(max(count))
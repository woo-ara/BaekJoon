'''
백준 13460 구슬 탈출2
22.11.16 우아라

빨, 파 하나씩 넣고 빨강을 구멍으로 빼기 ->중력으로 왼,오,위,아래
세로 n 가로 m  1x1행

'''





'''

import sys
from collections import deque

def init(graph,n,m):
    rx, ry, bx, by = 0, 0, 0, 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 'R':
                rx, ry = i, j
            elif graph[i][j] == 'B':
                bx, by = i, j
    queue.append((rx, ry, bx, by, 1))
    check[rx][ry][bx][by] = True

def move(x, y, dx, dy):
    nx = x
    ny = y
    move_cnt = 0
    while True:     # 한 방향으로 이동할 수 있을 때까지 이동시키기
        if graph[nx+dx][ny+dy] != '#' and graph[nx+dx][ny+dy] != 'O':
            nx += dx
            ny += dy
            move_cnt += 1
        else:
            break
    return nx, ny, move_cnt

def bfs(graph, len, wid):
    init(graph, len, wid)

    while queue:    # 큐가 완전히 빌 때까지 반복
        rx, ry, bx, by, depth = queue.popleft() # 큐에 삽입된 순서대로 노드 하나 꺼내기
        if depth > 10:
            break
        for i in range(4):  #이동한 구슬 위치
            nrx, nry, rcnt = move(rx, ry, dx[i], dy[i])
            nbx, nby, bcnt = move(bx, by, dx[i], dy[i])

            if graph[nbx][nby] != 'O':
                # 빨간구슬이 구멍위라면 끝
                if graph[nrx][nry] == 'O':
                    print(depth)
                    return
                if nrx == nbx and nry == nby:
                    if rcnt > bcnt:
                        nrx -= dx[i]
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]
                if not check[nrx][nry][nbx][nby]:
                    check[nrx][nry][nbx][nby] = True
                    queue.append((nrx, nry, nbx, nby, depth + 1))
    return -1
    # print(-1)



input = sys.stdin.readline


if __name__ == '__main__':
    n, m = map(int, input().split())  # 세로, 가로

    graph = []
    for i in range(n):  #보드 모양 '.', '#', 'O', 'R', 'B'
        graph.append(list(input().strip()))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()   # 큐 구현을 위한 deque 라이브러리

    check = [[[[False]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]

    ans = bfs(graph, n, m)

    print(ans)

'''


#현재의 좌표 x,y // 이동할만큼의 거리 dx,dy
def move(x,y,dx,dy):
    cnt = 0
    # 현재내위치의 인접이 벽이거나, 내위치가 구슬이면 이동안하도록
    # 즉 move함수를 수행했을때 구슬의위치는 구멍 위거나 벽 바로옆
    while graph[x+dx][y+dy] != '#' and graph[x][y] != 'O':
        x += dx
        y += dy
        cnt +=1
    return x,y,cnt

def bfs(graph, n,m):
    rx, ry, bx, by = 0, 0, 0, 0 #위치 초기화
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 'R':  #빨간구슬 위치
                rx, ry = i, j
            elif graph[i][j] == 'B':    #파란구슬 위치
                bx,by = i,j

    q.append((rx, ry, bx, by, 1))
    check[rx][ry][bx][by] = True

    while q:
        rx, ry, bx, by, depth = q.popleft()
        if depth > 10:  #10회 이상이면 끝
            break
        for i in range(4):
            # 이동한 빨간구슬과 파란구슬의 위치
            nrx, nry, rcnt = move(rx, ry, dx[i], dy[i])
            nbx, nby, bcnt = move(bx, by, dx[i], dy[i])
            # 파란구슬이 구멍위가 아니면서 ( 구멍위면 다른방향으로 이동해야함 )
            if graph[nbx][nby] != 'O':
                # 빨간구슬이 구멍위라면 끝
                if graph[nrx][nry] == 'O':
                    print(depth)
                    return
                if nrx==nbx and nry==nby:
                    if rcnt>bcnt:
                        nrx -= dx[i]
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]
                if not check[nrx][nry][nbx][nby]:
                    check[nrx][nry][nbx][nby] = True
                    q.append((nrx,nry,nbx,nby, depth+1))
    print(-1)


import sys
from collections import deque

input = sys.stdin.readline

# 가로(열), 세로(행) - m,n

graph = []
n,m = map(int, input().split())

for i in range(n):
    temp = list(input().strip())
    graph.append(temp)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque()

    # 방문처리해줄 4차원 배열
check = [[[[False]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]

bfs(graph, n, m)








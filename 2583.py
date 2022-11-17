'''
백준 2583 영역 구하기
22.11.16 우아라
'''

import sys
sys.setrecursionlimit(10 ** 6)    #재귀 최대깊이 설정

m, n, k = map(int, input().split())    #모눈종이 오른쪽 위 꼭짓점, 입력 k개 직사각형
graph = [[0] * n for i in range(m)]    #그림그리기

rec = []  #k개 직사각형
for i in range(k):
    rec.append(list(map(int, input().split())))

for point in rec:     #그림에 1로 표시
    for x in range(point[0], point[2]):
        for y in range(point[1], point[3]):
            graph[y][x] = 1

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]  #상하좌우ㅌ

#분리된 영역의 크기
def dfs(x, y, cnt):
    graph[x][y] = 1
    for dx, dy in d:
        X, Y = x + dx, y + dy
        if 0 <= X < m and 0 <= Y < n and graph[X][Y] == 0:
            cnt = dfs(X, Y, cnt+1)
    return cnt

#분리된 영역 구하기
res = []
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            res.append(dfs(i, j, 1))

print(len(res))
print(*sorted(res))




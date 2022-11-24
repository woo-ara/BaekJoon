'''
백준 1743 음식물 피하기
22.11.23 우아라
'''

# n, m, k = map(int, input().split())
#
# rc = []
# for i in range(k):
#     rc.append(map(int, input().split()))


import sys
from collections import deque

input = sys.stdin.readline
dx = [0, 0, -1, 1]  #상하좌우
dy = [-1, 1, 0, 0]  #상하좌우

def bfs(i, j, trash):
    q = deque([[i, j]])
    trash[i][j] = 2  # 방문한 쓰레기
    result = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 < nx <= n and 0 < ny <= m and trash[nx][ny] == 1:
                q.append([nx, ny])
                trash[nx][ny] = 2
                result += 1
    return result

n, m, k = map(int, input().split())
trash = [[0] * (m + 1) for _ in range(n + 1)]

answer = 0  #총 쓰레기 개수

for _ in range(k):
    x, y = map(int, input().split())
    trash[x][y] = 1

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if trash[i][j] == 1:
            ans = bfs(i, j, trash)
            answer = max(ans, answer)

print(answer)
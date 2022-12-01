'''
백준 1890 점프
22.12.01 우아라
'''

N = int(input())
jump_map = [[int(n) for n in input().split()] for _ in range(N)] # 점프맵 생성
dp = [[0 for _ in range(N)] for _ in range(N)] # dp맵 생성
dp[0][0] = 1 #dp 초기값에 1을 넣어줌으로써 경우의 수 시작
for i in range(N) :
    for j in range(N) :
        if i == N-1 and j == N-1 :
            break
        jump = jump_map[i][j]
        ax = i + jump
        ay = j + jump
        # 다음 도착지에 현재 위치까지 오는 경우의 수를 저장
        if ax < N :
            dp[ax][j] += dp[i][j]
        if ay < N :
            dp[i][ay] += dp[i][j]
print(dp[-1][-1])


'''
n = int(input())
dp = [[0] * n for _ in range(n)]

for i in range(n):
'''


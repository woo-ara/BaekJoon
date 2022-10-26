'''
백준 2847 - 게임을 만든 동준이
22.10.26 우아라
'''

n = int(input())    #레벨

score = []  #점수
for i in range(n):
    s = int(input())
    score.append(s)

# score_last = score[-1]
score.reverse() #점수 배열을 거꾸로 뒤집기

# 5 4 3

for i in range(n-1):
    # s1 = score[i]
    # s2 = score[i-1]
    num1 =
    num2 =
    sub = s1 - s2
    if sub < 0:

    elif sub == 0:
        s2 = s1 - 1





ans = []
ans.append(score_last)
for i in range(n - 1):
    sl = score_last - 1
    ans.append(sl)
    score_last = score_last - 1

cnt = 0
for i in range(n):
    cnt += score[i] - ans[i]

print(cnt)
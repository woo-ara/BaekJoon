'''
백준 2847 - 게임을 만든 동준이
22.10.26 우아라
'''

n = int(input())    #레벨 입력

score = []  #점수 입력
for i in range(n):
    s = int(input())
    score.append(s)

score.reverse() #점수 배열을 거꾸로 뒤집기

cnt = 0

for i in range(n-1):
    num1 = score[i]
    num2 = score[i+1]
    sub = num2 - (num1 - 1) # (뒷배열)은 (앞배열 - 1) 과 작거나 같아야함
    if sub > 0: # 만약 크다면
        cnt = cnt+sub   # 차이만큼 cnt에 +
        score[i+1] = score[i] - 1   # (뒷배열)을 (앞배열 -1) 로 값 변경

print(cnt)
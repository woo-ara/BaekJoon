'''
백준 1700 멀티탭 스케줄링
22.10.27 우아라
'''


n, k = map(int, input().split())    #멀티탭 구멍 개수, 전기용품 총 사용횟수
k_list = list(map(int, input().split()))
socket = [0] * n
cnt = 0
idx = 0
tmp = 0
tmp_i = 0

n, k = map(int, input().split())    #멀티탭 구멍 개수, 전기용품 총 사용횟수
k_list = list(map(int, input().split()))
socket = [0] * n
cnt = 0
idx = 0
tmp = 0
tmp_i = 0

for i in k_list:
    if i in socket: # 플러그 이미 꽂혀있으면
        pass
    elif 0 in socket:   # 구멍 빈자리 있는 경우
        socket[socket.index(0)] = i # 그 자리에 꽂기
    else:   # 빈자리 없어서 뽑고 꽂아야 하는 경우
        for j in socket:
            if j not in k_list[idx:]:   # 더이상 사용되지 않으면
                tmp = j # 뽑기
                break
            elif k_list[idx:].index(j) > tmp_i: # 나중에 다시 사용되면
                tmp = j
                tmp_i = k_list[idx:].index(j)    # 더 나중에 사용되는 것 뽑기
        socket[socket.index(tmp)] = i   # tmp 번째 자리에 꽂기
        tmp = tmp_i = 0 #초기화
        cnt += 1
    idx += 1

print(cnt)






'''
socket = []
list1 = []
for i in range(0, k, n):    # 리스트를 n개씩 묶기
    socket.append(k_list[i: i + n])
    socket = list(socket)
    
cnt = 0
for i in range(n - 1):
    for j in range(len(socket[i+1])):
        if len(socket[i+1]) != n: # 배열 길이가 n이 아니면
            cnt = cnt - 1
        # if socket[i][j] # 배열 길이가 1이면

        if socket[i + 1][j] not in socket[i]:
            # if
            cnt += 1

if cnt < 0:
    print(0)
else:
    print(cnt)
'''
'''
22.10.03 우아라
백준 1449 수리공 항승
'''


n, l = map(int, input().split())    # 물이 새는 곳 수, 테이프의 길이
loc = list(map(int, input().split()))   # 물이 새는 위치

loc.sort()

cnt = 0
copy_l = l

for i in range(int(n-1)):

    len = loc[i+1] - loc[i] + 1  # len은 (다음+0.5) - (이전-0.5)

    if len < l:  # len이 1보다 작으면
        l = l - len

    elif len == l:   # len이 1이면
        cnt += 1
        l = copy_l

    else:
        l = copy_l
        continue
    # else:
    #     cnt += len // l
    #     len %= l

print(cnt)


'''
     1     2          100      101
 0.5   1.5  2.5   99.5   100.5    101.5
 1-------------   2--------------------
 
 
 
     1     2     3     4
  0.5  1.5   2.5   3.5   4.5
  1-------------------   2---   
    

     3       2       1
     1       2       3
  0.5  1.5      2.5    3.5
  1------ 2------- 3------



'''



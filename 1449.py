'''
22.10.03 우아라
백준 1449 수리공 항승
'''

'''
n, l = map(int, input().split())    # 물이 새는 곳 수, 테이프의 길이
loc = list(map(int, input().split()))   # 물이 새는 위치

loc.sort()

cnt = 0
copy_l = l

a = []
for i in range(int(n - 1)):
    len = loc[i + 1] - loc[i]
    a.append(len)


# add_len = 0
kk = 0

if int(l) == 1:
    print(n)

else:
    for i in range(int(n - 1)):
        save_a = a[i]

        # 만약 len 이 테이프 길이(l) 와 같으면 n - 1
        if (save_a + 1) == l:
            cnt += 1
            print(str(i) , ' 번째 : len이 테이프의 길이와 같음 ')
            print( 'n : ', n)

        elif (save_a + 1) > l:
            print(str(i), ' 번째 : len이 테이프의 길이보다 크기 때문에 그냥 넘어감 ')
            print('n : ', n)
            continue

        else:
            #save_a 가 l 이랑 같거나 넘을때까지, 근데 넘으면 n 한번 다시 +1
            print(str(i), ' 번째 : len이 테이프의 길이보다 작음 - if or else 들어감')
            print('n : ', n)

            j = i
            # kk = a[j]
            while (kk + 1) < l:
                print('while문 시작')
                kk += a[j]
                j += 1
                print('kk : ', kk)
            print('j : ', j)
            i = j

            if (kk + 1) % l == 0:
                print(str(i), ' 번째 : if문 - len % l 나머지가 0이기 때문에 그리디')
                # cnt += (kk + 1) // l
                # n = n - cnt
                cnt += 1
                print('n : ', n)

            else:
                print(str(i), ' 번째 : else문 - len % l 나머지가 0이 아니기 때문에 그리디에서 n+1')
                # cnt += (kk + 1) // l
                # n = n - (cnt - 1)
                cnt += 1
                print('n : ', n)
    print(cnt)
'''


N,L = map(int,input().split())

tape = list(map(int,input().split()))

tape.sort()

loc = 0
cnt = 0

for i in tape:
    if loc < i:
        loc = i+L-1
        cnt += 1

print(cnt)

'''
       1      2             100       101
 (0.5)   (1.5)  2.5   (99.5)   (100.5)    101.5
 1------------------   2-----------------------
 
 
     1     2     3     4
  0.5  1.5   2.5   3.5   4.5
  1-------------------   2---   
    

     3       2       1
     1       2       3
  0.5  1.5      2.5    3.5
  1------ 2------- 3------

'''

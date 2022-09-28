'''
22.09.28 우아라
백준 1012
'''

case = int(input())

list_mn = []
list_k = []
answer = []

for i in range(case):
    list_mn.append(list(map(int, input().split()) ) )
    for j in range(int(list_mn[i][-1])):
        list_k.append( [i] + list(map(int, input().split())))


for i in range(case):
    print('case : ', i)
    n = list_mn[i][-1]
    print('n : ', n)
    list_k.sort(key=lambda x: x[1]) # x축 같은 것끼리 모으기
    print(list_k)
    for k in range((list_mn[i][-1]) -1):
        if (list_k[k][0] == i) & (list_k[k][1] == list_k[k+1][1]):
            if (list_k[k][2]) == (list_k[k+1][2] -1):   # 만약 y축이 1 차이나면 +1
                # if ( ) != ( )                          #근데 ...이면 안됨
                n = n-1
                print('x', n)

    list_k.sort(key=lambda x: x[2]) # y축 같은 것끼리 모으기
    for k in range(list_mn[i][-1] - 1):
        if (list_k[k][0] == i) & (list_k[k][2] == list_k[k + 1][2]) & (list_k[k][1] == list_k[k + 1][1]-1):
            # if (list_k[k][1] == list_k[k + 1][1]-1):  # 만약 x축이 1 차이나면 +1
            n = n-1
            print('y', n)
    answer.append(n)

print(answer)


# 0 0

# 1 0
# 1 1

# 2 4

# 3 4

# 4 2
# 4 3
# 4 5

# 7 4
# 7 5
# 7 6

# 8 5
# 8 4
# 8 6

# 9 4
# 9 5
# 9 6




########


# 0 0
# 1 0

# 1 1

# 4 2

# 4 3

# 2 4
# 3 4
# 7 4
# 8 4
# 9 4

# 4 5
# 7 5
# 8 5
# 9 5

# 7 6
# 8 6
# 9 6

7




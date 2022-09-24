'''
22.09.22 우아라
백준 7568

덩치 : (x,y)
x, y 비교
'''

import sys


# 입력
n = int(input())
read = sys.stdin.readline
dc = []

for i in range(n):
  dc.append(list(map(int, read().split())))
  # dc.append(list(map(int, read().split()))+[0])
# print(dc)


# print(dc)
# 46,   55,   58,   60,   88
#
# 155   185   183   175   186
#
# 5     2     2      2     1

# 1    2       3      4     5
# 1    4       3      2     5

# 2    6      6      6     10





score = n
score_list = []

# x 점수 부여
for i in range(n-1):

    # if dc[i][1] <= dc[i + 1][1]:
    #     score = score - 1
    else:
        score = score - 0

    score_list.append(score)
score_list.append(score)


def search_list(a, x):
    n = len(a)


for i in range(0, n):
    if x == a[i]:
        return i
return -1

v = [17, 92, 18, 33, 58, 7, 33, 42]
print(search_list(v, 18))  # 2



# x 오름차순 나열
# dc.sort(key=lambda x:x[0])

# print(dc)

# score = n
# score_list = []

# y가 전보다 작으면 -1, 계속 작으면 계속 -1 후 모두 같은 등수

#
#
# for i in range(n-1):
#
#     # if dc[i][1] <= dc[i + 1][1]:
#     #     score = score - 1
#     else:
#         score = score - 0
#
#     score_list.append(score)
# score_list.append(score)

print(score_list)

# 등수가 1일때까지.





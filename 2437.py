'''
22.10.05 우아라
백준 2437 - 저울
'''

'''
# 메모리 초과

from itertools import permutations

N = int(input())    #저울추 개수
W = list(map(int, input().split())) #저울추 무게

set(W)

w_list = []
for i in range(N):
    w = (list(permutations(W, i)))
    for j in w:
        w_sum = sum(j)
        w_list.append(w_sum)

w_list = set(w_list)

num = 0
for i in w_list:
    while num in w_list:
        num += 1

print(num)
'''

'''
from itertools import combinations

N = int(input())    #저울추 개수
W = list(map(int, input().split())) #저울추 무게

w_list = []
for i in range(N):
    w = (list(combinations(W, i)))
    for j in w:
        w_sum = sum(j)
        w_list.append(w_sum)

w_list = set(w_list)

num = 0
for i in w_list:
    if num != i:
        break
    else:
        num += 1

print(num)
'''



N = int(input())    #저울추 개수
W = list(map(int, input().split())) #저울추 무게

W.sort()

num = 1
for i in W:
    if num < i:
        break
    else:
        num += i

print(num)






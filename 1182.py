'''
백준 1182 부분수열의 합
22.11.08 우아라
'''

from itertools import chain, combinations

n, s = map(int, input().split())
num_list = list(map(int, input().split(maxsplit=n)))
com_list = list(chain.from_iterable(combinations(num_list, r) for r in range(1, len(num_list) + 1)))    #모든 조합 구하기

sum_list = []
cnt = 0
for i in range(len(com_list)):  #조합의 합이 s 이면 cnt++
    if sum(com_list[i]) == s:
        cnt += 1
print(cnt)
'''
백준 1182 부분수열의 합
22.11.08 우아라
'''

from itertools import chain, combinations

n, s = map(int, input().split())    #정수개수, 합

s_list = []
s_list.append(map(int, input().split()))

# s_list.sort()
com_list = chain.from_iterable(combinations(s_list, r) for r in range(1, len(s_list + 1)))

print(com_list)

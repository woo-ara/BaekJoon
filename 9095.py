'''
백준 9095 1,2,3 더하기
22.11.24 우아라
'''

import sys
read = sys.stdin.readline

cache = [0] * 11
cache[1] = 1
cache[2] = 2
cache[3] = 4

for i in range(4, 11):
    cache[i] = sum(cache[i-3:i])

T = int(read())
for _ in range(T):
    print(cache[int(read())])

'''
# O(n)
fibo_arr = [0, 1, 2, 4] # memoization

def topdown_fibo(n):
    if n < len(fibo_arr):
		print(fibo_arr[n])
    else:
		fibo = topdown_fibo(n-1) + topdown_fibo(n-2)
		fibo_arr.append(fibo)
		print(fibo)

t_list = []
t = int(input())
for i in range(t):
    t_list.append(int(input()))

for i in range(t):
	
'''



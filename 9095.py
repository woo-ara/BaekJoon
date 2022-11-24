'''
백준 9095 1,2,3 더하기
22.11.24 우아라
'''

# O(n)
fibo_arr = [0, 1, 2, 4] # memoization

def topdown_fibo(n):
    if n < len(fibo_arr):
		print(fibo_arr[n])
    else:
        for i in range(n):
            t_list[i]
		fibo = topdown_fibo(n-1) + topdown_fibo(n-2)
		fibo_arr.append(fibo)
		print(fibo)

t_list = []
t = int(input())
for i in range(t):
    t_list.append(int(input()))

for i in range(t):



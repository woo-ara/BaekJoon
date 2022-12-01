'''
백준 1309 동물원
22.11.30 우아라
'''

n = int(input())

dp = [[0] * 3 for _ in range(n+1)]
d = 9901

for i in range(3):
    dp[1][i] = 1

for i in range(2, n+1):
    dp[i][0] = dp[i-1][1] % d + dp[i-1][2] % d
    dp[i][1] = dp[i-1][0] % d + dp[i-1][2] % d
    dp[i][2] = dp[i-1][0] % d + dp[i-1][1] % d + dp[i-1][2] % d

print(sum(dp[n]) % d)


'''
n = int(input())

dp = [1 for _ in range(n+1)]

# print(dp)
dp[1] = 3

if n == 1:
    print(dp[1])
else:
    for i in range(2, n+1):
        dp[i] = dp[i-2] + (dp[i-1] * 2)
        dp[i] %= 9901
    print(dp[n])
'''


'''
* ㅇ
ㅇ *
* ㅇ
ㅇ *

8 +[ 6(3+3) +   4    + 2   ]+ [4 + 4 +] 2    
n +[ 대각선   + 대각선2 +  대3 ]+ [    
10 20 30

8    6  4  2    12   2  = 34
     4  2  

1
1x8
2x2  2x1  2x2  2x1  2x3
2x2   
'''
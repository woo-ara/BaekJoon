'''
22.09.29 우아라
백준 1463
'''

# n = int(input())
# n2 = n
# n3 = n
#
# count = 0
#
# way = [3, 2]
# answer = []
#
# while n > 1:
#     if (n % 3 == 0) & (n % 2 == 0):
#         for i in way:
#             count += n//i
#             n %= i
#     elif (n % 3 == 0) & (n % 2 != 0):
#         count += n // 3
#         n %= 3
#     elif (n % 3 != 0) & (n % 2 == 0):
#         count += n // 2
#         n %= 2
#     else:
#         n = n - 1
#         count += 1
# answer.append(count)
#
#
# count = 1
# n2 = n2 - 1
# while n2 > 1:
#     if (n2 % 3 == 0) & (n2 % 2 == 0):
#         for i in way:
#             count += n2//i
#             n2 %= i
#     elif (n2 % 3 == 0) & (n2 % 2 != 0):
#         count += n2 // 3
#         n2 %= 3
#     elif (n2 % 3 != 0) & (n2 % 2 == 0):
#         count += n2 // 2
#         n2 %= 2
#     else:
#         n2 = n2 - 1
#         count += 1
# answer.append(count)
#
# count = 2
# n3 = n3 - 2
# while n3 > 1:
#     if (n3 % 3 == 0) & (n3 % 2 == 0):
#         for i in way:
#             count += n3//i
#             n3 %= i
#     elif (n3 % 3 == 0) & (n3 % 2 != 0):
#         count += n3 // 3
#         n3 %= 3
#     elif (n3 % 3 != 0) & (n3 % 2 == 0):
#         count += n3 // 2
#         n3 %= 2
#     else:
#         n3 = n3 - 1
#         count += 1
# answer.append(count)
#
# while 0 in answer:
#     answer.remove(0)
# print(min(answer))
#
#
#
# 11
#
# 10
#
# 9
#
# 3
#
# 1




# n = int(input())
# n2 = n-1
# n3 = n-1
# n4 = n-2
# n5 = n-2
#
#
# answer = []
#
# count = 0
# while n > 1:
#     if (n % 3 == 0) & (n % 2 == 0):
#         for i in way:
#             count += n//i
#             n %= i
#             if n == 1:
#                 count -= 1
#     elif (n % 3 == 0) & (n % 2 != 0):
#         count += n // 3
#         n %= 3
#     elif (n % 3 != 0) & (n % 2 == 0):
#         count += n // 2
#         n %= 2
#     else:
#         n = n - 1
#         count += 1
# print('1', count)
# answer.append(count)
#
#
# count = 1
# while n2 > 1:
#     if (n2 % 3 == 0) & (n2 % 2 == 0):
#         for i in way:
#             count += n2//i
#             n2 %= i
#             if n2 == 1:
#                 count -= 1
#     elif (n2 % 3 == 0) & (n2 % 2 != 0):
#         count += n2 // 3
#         n2 %= 3
#     elif (n2 % 3 != 0) & (n2 % 2 == 0):
#         count += n2 // 2
#         n2 %= 2
#     else:
#         n2 = n2 - 1
#         count += 1
# print('2', count)
# answer.append(count)
#
# n2 = n3
# count = 1
# while n2 > 1:
#     if (n2 % 3 == 0) & (n2 % 2 == 0):
#         for i in way:
#             count += n2//i
#             n2 %= i
#             if n2 == 1:
#                 count -= 1
#             print('a', count)
#     elif (n2 % 3 != 0) & (n2 % 2 == 0):
#         count += n2 // 2
#         n2 %= 2
#         if n2 == 1:
#             count -= 1
#         print('b', count)
#     elif (n2 % 3 == 0) & (n2 % 2 != 0):
#         count += n2 // 3
#         n2 %= 3
#         print('n2 : ', n2)
#         if n2 == 1:
#             count -= 1
#         print('c', count)
#     else:
#         n2 = n2 - 1
#         count += 1
#         print('d', count)
# print('3', count)
# answer.append(count)
#
# n3 = n4
# count = 2
# while n3 > 1:
#     if (n3 % 3 == 0) & (n3 % 2 == 0):
#         for i in way:
#             count += n3//i
#             n3 %= i
#             if n3 == 1:
#                 count -= 1
#     elif (n3 % 3 == 0) & (n3 % 2 != 0):
#         count += n3 // 3
#         n3 %= 3
#     elif (n3 % 3 != 0) & (n3 % 2 == 0):
#         count += n3 // 2
#         n3 %= 2
#     else:
#         n3 = n3 - 1
#         count += 1
# print('4', count)
# answer.append(count)
#
# n3 = n5
# count = 2
# while n3 > 1:
#     if (n3 % 3 == 0) & (n3 % 2 == 0):
#         for i in way:
#             count += n3//i
#             n3 %= i
#             if n3 == 1:
#                 count -= 1
#     elif (n3 % 3 != 0) & (n3 % 2 == 0):
#         count += n3 // 2
#         n3 %= 2
#     elif (n3 % 3 == 0) & (n3 % 2 != 0):
#         count += n3 // 3
#         n3 %= 3
#     else:
#         n3 = n3 - 1
#         count += 1
# print('5', count)
# answer.append(count)
#
# while 0 in answer:
#     answer.remove(0)
#
# print(min(answer))



n = int(input())

# n+1개 만큼의 0으로 이루어진 배열 만들기
# dp = [0] * (n+1)
dp = [0 for _ in range(n+1)]

for i in range(2, n+1):
    # 2와 3으로 나누어 떨어지지 않으면 횟수+1
    dp[i] = dp[i-1] + 1

    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)

print(dp[n])



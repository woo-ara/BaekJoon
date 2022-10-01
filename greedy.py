

# n = 960
# count = 0
#
# array = [500, 100, 50, 10]
#
# for coin in array:
#     count += n//coin
#     n %= coin
#
# print(count)

n, k = map(int,input().split())
count = 0

a_list = []
for i in range(n):
    a_list.append(int(input()))

a_list.sort(reverse=True)

for coin in a_list:
    count += k // coin
    k %= coin

print(count)

#
#
#
# n = 960
# count = 0
#
# array = [500, 100, 50, 10]
#
# for coin in array:
#     count += n//coin
#     n %= coin
#
# print(count)







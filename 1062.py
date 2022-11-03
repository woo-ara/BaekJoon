'''
백준 1062 가르침
2022.11.03 우아라
'''

n, k = map(int, input().split())

letter = ['a', 'n', 't', 'i', 'c']

word = []
for i in range(n):
    str1 = input()
    list1 = list(str1)
    word.append(list1)
word.sort(key=len)  # 여기서 겹치는 문자 먼저 제거하고 수를 비교해야할 듯

for i in word:
    for j in range(len(i)):
        if i[j] not in letter:
            letter.append(i[j])

letter = letter[:k]

ans = 0
for i in word:
    cnt = 0
    for j in i:
        if j in letter:
            cnt = cnt + 1
    if cnt == len(i):
        ans = ans + 1
print(ans)



'''

3 6
anta rc tica
anta hello tica
anta car tica


rc
hello
car

a n t i c / r h e l o
->2



xxxxxxx
rc

a n t i c / x r c 
-> 
'''


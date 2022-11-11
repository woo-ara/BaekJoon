'''
백준 1759 암호 만들기
22.11.10 우아라
'''

from itertools import *

l, c = map(int, input().split())    #알파벳개수, 문자종류
c_letter = list(input().split(maxsplit=c))

vow = ['a', 'e', 'i', 'o', 'u'] #vowel
vow_len = 0
vow_list = []
for i in vow:
    if i in c_letter:
        vow_len += 1        #모음 개수
        vow_list.append(i)  #모음 리스트

con_len = l - vow_len #consonant
con_list = list(set(c_letter) - set(vow_list))  #자음 리스트

vow_ans = list(combinations(vow_list, 1))   #모음에서 1개씩 뽑기
con_ans = list(combinations(con_list, 2))   #자음에서 2개씩 뽑기

ans_list = []
for i in vow_ans:
    ans = []
    for j in con_ans:
        k_list = list(set(c_letter) - set(i) - set(j))
        k_ans = list(combinations(k_list, (l - 3)))
        for k in k_ans:
            ans = list(i + j + k)   #모음1 + 자음2 + 나머지(l-3) 개
            ans.sort()
            ans_list.append(''.join(ans))

ans_list = list(set(ans_list))
ans_list.sort() #사전순 정렬

for i in ans_list:
    print(i)







'''
vow = ['a', 'e', 'i', 'o', 'u'] #vowel
alphabet = list(ascii_lowercase)
vow_len = 0
vow_list = []
for i in vow:
    if i in c_letter:
        vow_len += 1
        vow_list.append(i)
        
con_len = l - vow_len #consonant
con_list = list(set(c_letter) - set(vow_list))

vow_ans = []
con_ans = []
# for i in range(vow_len):
vow_ans.append(list(combinations(vow_list, 1)))
# for i in range(con_len):
con_ans.append(list(combinations(con_list, 2)))
'''











'''
ans = []
if vow_len == 1:
    a = Counter(c_letter)
    b = a.most_common(l - 1)
    for i in range(len(b)):
        ans = vow_list[0] + b[i]
        ans.sort()
        print(ans)
else:
    while con_len < 2:
        for i in range(l):





v = ['a', 'e', 'i', 'o', 'u']
alphabet = list(ascii_lowercase)

v_len = 0
v_list = []
for i in v:
    if i in c_letter:
        v_len += 1
        v_list.append(i)
        
ans = []
def answer(idx):
    for i in range(c):
        if c_letter[i] == 'a' | 'e' | 'i' | 'o' | 'u':
            ans.append(v_list[i])
        else:
            ans.append(v_list[i])
        if len(ans) == l:
            print(ans)
            del ans[idx:]

for j in range(len())

#v_len > 1 이면 하나만 출력하거나 여러개 가능

#v_len == 1이면 무조건 출력, 앞, 뒤에오는 것 중 l-1개 출력 가능
if v_len == 1:
    ans.append(v_list[0])
    idx = alphabet.index(v_list[0])
    left_list = []
    right_list = []
    for i in range(idx):
        left_list.append(list(combinations(alphabet[:idx], i)))
        right_list.append(list(combinations(alphabet[idx:], i)))
'''



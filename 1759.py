'''
백준 1759 암호 만들기
22.11.10 우아라
'''

# 답 풀이
l, c = map(int, input().split())
bet = list(map(str, input().split()))
bet.sort() #알파벳 오름차순 정렬
vowels = ['a', 'e', 'i', 'o', 'u']
ans = []

def check(ans):
    mo = 0 #모음 개수
    ja = 0 #자음 개수
    for i in range(l): #개수 계산
        if ans[i] in vowels:
            mo += 1
        else:
            ja += 1
    if mo >= 1 and ja >= 2: #자음모음 개수 충족
        return True
    else:
        return False
def func(j):
    if len(ans) is l:
        if check(ans) is False: #자음모음 개수 조건 확인
            return
        for i in ans: #출력
            print(i, end="")
        print()
        return
    for i in range(j, c): #알파벳 오름차순 정렬(j)
        ans.append(bet[i])
        func(i+1)
        ans.pop()
func(0)


'''
# 내 풀이

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









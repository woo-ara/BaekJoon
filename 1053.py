'''
백준 1053 팰린드롬 공장
22.11.03 우아라
'''
# 1) 삽입 or 삭제 -> 삭제로 통일
# 2) 다른 문자로 교환
# 3) 서로 교환 (한번만) - 이거먼저

from itertools import combinations

def rec(l, r):
    if (l >= r):
        return 0

    ret = dp[l][r]
    if (ret != -1):
        return ret

    ret = 1000000000
    if (letter[l] == letter[r]):  # 만약 letter[l] == letter[r] 이면 dp[l+1][r-1] 고려
        ret = rec(l+1, r-1)

    ret = min((dp[l][r], rec(l+1, r) + 1), (rec(1, r-1) + 1))
    # dp[l][r] = ret
    return ret


letter = input()
letter_len = len(letter)
dp = [[-1]*51 for _ in range(51)]

answer = rec(0, letter_len - 1)

for i in range(letter_len):
    for j in range(i+1, letter_len):
        letter[j], letter[i] = letter[i], letter[j] #swap
        dp = [[-1] * 51 for _ in range(51)]
        answer = min(answer, rec(0, letter_len - 1) + 1)
        letter[j], letter[i] = letter[i], letter[j] #swap

print(answer)










'''
from itertools import combinations

def swap_char(a, b, st):
    c = st[b]
    st = st[:b] + st[a] + st[b+1:]
    st = st[:a] + c + st[a+1:]
    return st

def factory(start_idx, end_idx, string):
    if cache[start_idx][end_idx] != -1:
        return cache[start_idx][end_idx]

    while start_idx < end_idx:
        if string[start_idx] == string[end_idx]:
            start_idx += 1
            end_idx -= 1
        else:
            break

    if start_idx >= end_idx:
        return 0

    ret = 1000000000
    ret = min(
        ret,
        factory(start_idx + 1, end_idx, string) + 1,
        factory(start_idx, end_idx - 1, string) + 1,
        factory(start_idx + 1, end_idx - 1, string) + 1
    )
    cache[start_idx][end_idx] = ret
    return ret


S = input()
s_len = len(S)

change_two = list(combinations([i for i in range(s_len)], 2))
answer = 1000000000
cache = [[-1]*51 for _ in range(51)]
answer = min(answer, factory(0, s_len-1, S))
for com in change_two:
    cache = [[-1] * 51 for _ in range(51)]
    s = swap_char(com[0], com[1], S)
    answer = min(answer, factory(0, s_len-1, s) + 1)
print(answer)
'''










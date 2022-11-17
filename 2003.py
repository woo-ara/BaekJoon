'''
백준 2003
'''


n, m = map(int, input().split())

a_list = list(map(int, input().split()))

cnt = 0
for i in range(1, n):
    tmp_val = sum(a_list[0:i])  #처음에 tmp_val에 n개씩 더함
    # ans_val = tmp_val

    # 처음에 k개만큼 더해줌
    for j in range(i, m):
        tmp_val = tmp_val + a_list[j] # 다음 인덱스 더해줌
        tmp_val = tmp_val - a_list[j - m] # 이전 인덱스 빼줌

        if tmp_val == m:
            cnt += 1
            # ans_val = tmp_val
        # max_val = max(tmp_val, max_val) # 더 큰값 구하기

        # print(ans_val)

print(cnt)




# tmp_val =



# print(a_list)



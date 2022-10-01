'''
22.09.29 우아라
백준 2606
'''

# compNum = int(input())
# compPair = int(input())
#
# comp_list = []
# for i in range(compPair):
#     comp_list.append(list(map(int, input().split())))
# # print(comp_list)  #[[1, 2], [2, 3], [1, 5], [5, 2], [5, 6], [4, 7]]
#
# list1 = sum(comp_list, [])
# # print(list1)  #[1, 2, 2, 3, 1, 5, 5, 2, 5, 6, 4, 7]
#
# visited = set()
# dup = {x for x in list1 if x in visited or (visited.add(x) or False)}
# # print(dup) # 1,2,5
# dup_list = list(dup)
# # print(list(dup))
#
# for i in range(len(comp_list)):
#     for j in dup_list:
#         if j in comp_list[i]:


n = int(input())    # 컴퓨터 수
m = int(input())    # 연결된 컴퓨터 쌍 수

#경로 저장 3차원 리스트
graph = [[] * n for _ in range(n + 1)]

#m개 간선을 입력받아 경로를 graph에 저장
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 다녀간 정점을 확인하기 위한 변수
cnt = 0
visited = [0] * (n + 1)

def dfs(start):
    global cnt
    visited[start] = 1
    for i in graph[start]:
        #들리지 않은 정점이면 dfs()를 이용하여 다시 반복
        if visited[i] == 0:
            dfs(i)
            cnt += 1

dfs(1)
print(cnt)







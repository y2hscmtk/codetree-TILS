n, m = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(n)]

result = 0

# 열에 대해서
for i in range(n):
    last = graph[i][0]
    count = 1
    if count == m:
        result += 1
        continue
    for j in range(1,n):
        if graph[i][j] == last:
            count+=1
        else: # 다를 경우
            last = graph[i][j]
            count = 1
        if count == m: # 목표한 수만큼 찾았으면 해당 방향에 대해서는 탐색 필요 없음
            result += 1
            break

# 행에 대해서
for i in range(n):
    last = graph[0][i]
    count = 1
    if count == m:
        result += 1
        continue
    for j in range(1,n):
        if graph[j][i] == last:
            count+=1
        else: # 다를 경우
            last = graph[j][i]
            count = 1
        if count == m: # 목표한 수만큼 찾았으면 해당 방향에 대해서는 탐색 필요 없음
            result += 1
            break

print(result)
        
n = int(input())
data = [list(map(int,input().split())) for _ in range(n)]


visited = [False]*n # 각 열의 숫자를 선택했는지 여부

select = [] # 선택된 숫자들

result = 1 # 정답
def find_max_value():
    global result
    result = max(result, min(select))
        

def dfs(cnt):
    if cnt == n: # n개 선택시 조건 검사
        find_max_value()
        return
    
    for i in range(cnt, n):
        for j in range(n):
            if not visited[j]:
                visited[j] = True
                select.append(data[i][j])
                dfs(cnt+1)
                select.pop()
                visited[j] = False
        return

dfs(0)
print(result)
n = int(input())
data = list(map(int,input().split()))

result = float('inf')
def dfs(curr, cnt): # 현재 위치, 점프 횟수(재귀 횟수)
    global result
    if curr >= n-1:
        if curr == n-1: # 원하는 위치에 도달
            result = min(result, cnt) # 최소 횟수 업데이트
        return
    
    # 현재 위치에서 최대 점프 가능 거리만큼 이동 가능
    if data[curr] > 0:
        for i in range(1,data[curr]+1):
            dfs(curr+i, cnt+1)

dfs(0,0)
print([result,-1][result == float('inf')])
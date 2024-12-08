n,m = map(int,input().split())

data = []

for _ in range(n):
    data.append(list(map(int,input().split())))

min_dist = float('inf')

def find_max_dist():
    large_dist = 0
    for i in range(m):
        x1,y1 = select[i]
        for j in range(i+1,m):
            x2,y2 = select[j]
            dist = (x1-x2)**2 + (y1-y2)**2
            large_dist = max(large_dist,dist)
    return large_dist

# 점 m개 고르기
select = []
def dfs(s,cnt):
    global min_dist
    if cnt == m:
        # 최대 중 최소거리 갱신
        min_dist = min(min_dist,find_max_dist())
        return
    
    for i in range(s, n):
        select.append(data[i])
        dfs(i+1,cnt+1)
        select.pop()

dfs(0,0)
print(min_dist)
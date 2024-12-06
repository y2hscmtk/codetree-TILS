n = int(input())
data = [list(map(int,input().split())) for _ in range(n)]
dx = [-1,0,1,0]; dy = [0,1,0,-1]
result = 0
def change_dir(t,d):
    if t == 0:
        return d
    if t == 1:
        if d == 0:
            return 1
        elif d == 1:
            return 0
        elif d == 2:
            return 3
        elif d == 3:
            return 2
    elif t == 2:
        if d == 0:
            return 3
        elif d == 1:
            return 2
        elif d == 2:
            return 1
        elif d == 3:
            return 0

def simulation(x,y,d):
    global result
    count = 1
    while True:
        nx, ny = x + dx[d], y + dy[d]
        if 0<=nx<n and 0<=ny<n:
            d = change_dir(data[nx][ny],d)
            count+=1
            x,y = nx,ny
        else:
            break
    result = max(result, count+1) # 빠져나갈때도 포함


# 위 방향
for i in range(n):
    simulation(0,i,2)
# -> 방향
for i in range(n):
    simulation(i,0,1)
# <- 방향
for i in range(n):
    simulation(i,n-1,3)
# 아래 방향
for i in range(n):
    simulation(n-1,i,0)


print(result)

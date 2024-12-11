# 숫자 1이 적힌 위치에서부터 숫자 n*n이 적힌 위치까지 교환 과정을 수행한다.
# 8개 인접한 방향으로 이동한다.

n,m = map(int,input().split())

grid = [list(map(int,input().split())) for _ in range(n)]

def in_range(x,y):
    if 0<=x<n and 0<=y<n:
        return True
    return False

def find_pos(num):
    for i in range(n):
        for j in range(n):
            if grid[i][j] == num:
                return (i,j)

def move(x,y):
    # 1. 8방향으로 인접한 수 중 가장 숫자가 큰 값과 위치 교환
    dsx = [-1,-1,-1,0,1,1,1,0]; dsy = [-1,0,1,1,1,0,-1,-1]
    last, next_x, next_y = 0,0,0
    for dx,dy in zip(dsx,dsy):
        nx,ny = x + dx, y + dy
        if in_range(nx,ny) and last<grid[nx][ny]:
            last = grid[nx][ny]
            next_x,next_y = nx,ny
    # 2. 위치 교환
    grid[x][y],grid[next_x][next_y] = grid[next_x][next_y],grid[x][y]


def simulation():
    # 1. 숫자 1이 적힌 숫자부터 숫자 n*n까지 이동
    for num in range(1,(n*n)+1):
        x,y = find_pos(num)
        move(x,y)
        


# m번의 턴 수행
for _ in range(m):
    simulation()

for row in grid:
    print(*row)
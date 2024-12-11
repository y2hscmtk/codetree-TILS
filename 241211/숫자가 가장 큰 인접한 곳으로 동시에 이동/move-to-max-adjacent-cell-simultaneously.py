'''
이동 조건 : 상하좌우 인접한 칸 중 가장 숫자가 큰 값, 동일한 값이 존재한다면 상하좌우 순으로 우선순위
격자를 벗어나서는 안된다.
이동 이후 2개 이상의 구슬 위치 동일할 경우 - 구슬은 모두 사라짐
'''
n,m,t = map(int,input().split())

board = [list(map(int,input().split())) for _ in range(n)]

grid = [[0]*n for _ in range(n)] # 현재 구슬의 위치는 1로 표시됨

next_grid = [[0]*n for _ in range(n)]

for _ in range(m):
    r,c = map(int,input().split())
    grid[r-1][c-1] = 1 # 구슬이 해당 자리에 존재함

# 격자 영역을 벗어나는지 검사
def in_range(x,y):
    if 0<=x<n and 0<=y<n:
        return True
    return False

def marble_move(x,y):
    # 상하좌우 이동
    dsx = [-1,1,0,0]; dsy = [0,0,-1,1]
    last_value = 0 # 격자 판의 숫자는 최소 1
    next_x,next_y = x,y
    for dx,dy in zip(dsx,dsy):
        nx,ny = x+dx,y+dy
        if in_range(nx,ny):
            # 상하좌우 숫자들 중 가장 큰 값으로 이동 가능
            if last_value < board[nx][ny]:
                last_value = board[nx][ny]
                next_x,next_y = nx,ny
    next_grid[next_x][next_y] += 1 # 구슬 1개 이동함


def simulation():
    # 1. next_grid 초기화
    for i in range(n):
        for j in range(n):
            next_grid[i][j] = 0
    
    # 2. 구슬 이동
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1: # 구슬이 존재한다면
                marble_move(i,j)
    
    # 3. 충돌한 구슬 제거
    for i in range(n):
        for j in range(n):
            if next_grid[i][j] >= 2:
                next_grid[i][j] = 0
    
    # 4. next_grid 값으로 grid 초기화
    for i in range(n):
        for j in range(n):
            grid[i][j] = next_grid[i][j]

# 시뮬레이션 t초간 수행
for _ in range(t):
    simulation()

# 남아있는 구슬 수 출력
marble_count = 0
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            marble_count += 1

print(marble_count)
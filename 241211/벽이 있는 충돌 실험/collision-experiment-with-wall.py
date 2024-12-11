t = int(input())

dx = [-1,0,1,0]; dy = [0,1,0,-1]
mapper = {'U':0,'R':1,'D':2,'L':3} # 방향 전환의 편의를 위해

def in_range(x,y):
    if 0<=x<n and 0<=y<n:
        return True
    return False

def move(x,y):
    d = grid[x][y]
    nx,ny = x + dx[d], y + dy[d]
    next_d = grid[x][y]
    # 1. 충돌한다면 방향 전환, 위치는 그대로
    if not in_range(nx,ny):
        next_d = (next_d + 2)%4
        next_pos = (x,y) # 위치는 그대로
    else: # 충돌하지 않는다면
        next_pos = (nx,ny)
    return (next_pos,next_d) # 다음 위치, 다음 방향
    


# 충돌이 발생하지 않는 횟수가 n번 반복된다면, 남아있는 구슬이 정해진 경로를 반복 운동 하고 있다는 의미가 되지 않을까?
def simulation():
    # 1. next_grid 초기화
    for i in range(n):
        for j in range(n):
            next_grid[i][j] = -1
    
    # 2. 각 구슬 이동
    for i in range(n):
        for j in range(n):
            if grid[i][j] != -1: # 해당 칸에 구슬이 존재한다면
                next_pos,next_d = move(i,j)
                next_x,next_y = next_pos
                if next_grid[next_x][next_y] != -1: # 구슬이 이미 존재하거나, 충돌나는 칸으로 이동시
                    next_grid[next_x][next_y] = -2 # 충돌 처리
                else: # 구슬이 위치하지 않는다면 - 충돌이 없다면
                    next_grid[next_x][next_y] = next_d
    
    # 3. 충돌난 구슬 제거
    for i in range(n):
        for j in range(n):
            if next_grid[i][j] == -2:
                next_grid[i][j] = -1

    # 4. next_grid의 값으로 grid 값 할당 - 구슬 이동 처리
    for i in range(n):
        for j in range(n):
            grid[i][j] = next_grid[i][j]


def get_marble_count():
    # 남아있는 구슬의 개수 출력
    marble_count = 0
    for i in range(n):
        for j in range(n):
            if grid[i][j] != -1:
                marble_count += 1
    return marble_count

for _ in range(t):
    n,m = map(int,input().split())
    grid = [[-1]*n for _ in range(n)]
    next_grid = [[-1]*n for _ in range(n)]
    # 구슬 초기 위치 입력
    for i in range(m):
        x,y,d = input().split()
        grid[int(x)-1][int(y)-1] = mapper[d]

    # 2*n 번 수행시 충돌 발생 불가 - 끝에서 끝까지 이동하는데 2*n 걸림
    for _ in range(2*n):
        simulation() # 시뮬레이션 수행

    print(get_marble_count())
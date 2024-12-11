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
    global crash_count
    # 1. next_grid 초기화
    for i in range(n):
        for j in range(n):
            next_grid[i][j] = -1
    
    # 2. 각 구슬 이동
    crash = False
    for i in range(n):
        for j in range(n):
            if grid[i][j] != -1: # 해당 칸에 구슬이 존재한다면
                next_pos,next_d = move(i,j)
                next_x,next_y = next_pos
                if next_grid[next_x][next_y] != -1:
                    next_grid[next_x][next_y] = -1 # 이미 구슬이 위치한다면 충돌 처리
                    crash = True
                else: # 구슬이 위치하지 않는다면 - 충돌이 없다면
                    next_grid[next_x][next_y] = next_d

    # 3. next_grid의 값으로 grid 값 할당 - 구슬 이동 처리
    for i in range(n):
        for j in range(n):
            grid[i][j] = next_grid[i][j]
    
    return crash # 충돌 여부 반환


for _ in range(t):
    n,m = map(int,input().split())
    grid = [[-1]*n for _ in range(n)]
    next_grid = [[-1]*n for _ in range(n)]
    # 구슬 초기 위치 입력
    for i in range(m):
        x,y,d = input().split()
        grid[int(x)-1][int(y)-1] = mapper[d]

    crash_count = 0
    while True:
        is_crash = simulation()
        # 충돌하지 않았다면
        if not is_crash:
            crash_count += 1
        else: # 충돌했다면 초기화
            crash_count = 0
        # 충돌하지 않은채로 n번 반복 했다면 끝에서 끝에 도달
        if crash_count == n:
            break
            
    # 남아있는 구슬의 개수 출력
    marble_count = 0
    for i in range(n):
        for j in range(n):
            if grid[i][j] != -1:
                marble_count += 1
    print(marble_count)
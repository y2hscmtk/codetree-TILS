'''
1. 인접한 숫자 중 가장 큰 값이 있는 위치로 이동
2. 8개의 방향 중 이동할 숫자가 없는 경우 이동 x
3. m번 움직인 이후의 상태 출력

좌표별 숫자의 위치 기록 - 비교용으로 사용
좌표별 뭉쳐진 숫자 기록 - 이동시 사용 
'''
n,m = map(int,input().split())

# 초기 좌표
grid = [list(map(int,input().split())) for _ in range(n)]

# 쌓여진 숫자들의 위치
num_grid = [[[] for _ in range(n)] for _ in range(n)]
# 초기에는 본인들의 숫자만 쌓여져 있음
for i in range(n):
    for j in range(n):
        num_grid[i][j].append(grid[i][j])

# 이동할 숫자들 
move_number = list(map(int,input().split()))

# 이동할 숫자의 위치 파악
def get_num_pos(num):
    for i in range(n):
        for j in range(n):
            for gm in num_grid[i][j]:
                if gm == num:
                    return (i,j)

# 영역 검사
def in_range(x,y):
    if 0<=x<n and 0<=y<n:
        return True
    return False

# 다음으로 이동할 위치 갱신
def get_next_pos(x,y):
    dx = [-1,-1,-1,0,1,1,1,0]
    dy = [-1,0,1,1,1,0,-1,-1]
    
    max_num = 0
    next_x,next_y = x,y # 다음에 이동할 위치
    for i in range(len(dx)):
        nx = x + dx[i]; ny = y + dy[i]
        # 영역 안에 존재하는 숫자들(존재x : 0)
        if in_range(nx,ny):
            if num_grid[nx][ny] and max_num < num_grid[nx][ny][-1]:
                max_num = num_grid[nx][ny][-1]  
                next_x,next_y = nx,ny
    return (next_x,next_y)


for num in move_number:
    x,y = get_num_pos(num)
    nx,ny = get_next_pos(x,y)

    new_stack = []
    left_stack = []
    find = False
    for i in range(len(num_grid[x][y])):
        next_num = num_grid[x][y][i]
        if next_num == num:
            new_stack.append(next_num)
            find = True
            continue
        if not find:
            new_stack.append(next_num)
        else:
            left_stack.append(next_num)
    
    num_grid[x][y] = left_stack
    num_grid[nx][ny] = new_stack + num_grid[nx][ny]


for i in range(n):
    for j in range(n):
        if num_grid[i][j]:
            print(*num_grid[i][j])
        else:
            print("None")

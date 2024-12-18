BLANK = 0

n,m = map(int,input().split())

grid = [list(map(int,input().split())) for _ in range(n)]

next_grid = [[0]*n for _ in range(n)]

def in_range(x,y):
    if 0<=x<n and 0<=y<n:
        return True
    return False

def simulation(c):
    dsx = [0,0,-1,1]; dsy = [-1,1,0,0]
    for i in range(n):
        for j in range(n):
            next_grid[i][j] = BLANK
    
    find = False
    # 해당 열의 가장 위 칸을 기준으로 터짐
    for row in range(n):
        if grid[row][c] != BLANK:
            r = row
            find = True
            break
    
    # 터질 폭탄이 존재하지 않는 경우는 아무런 일도 발생하지 않는다.
    if not find:
        return
    
    # 폭탄 터뜨리기
    target = grid[r][c]
    grid[r][c] = BLANK
    for t in range(target):
        for dx,dy in zip(dsx,dsy):
            nx = r + t*dx; ny = c + t*dy
            if in_range(nx,ny):
                grid[nx][ny] = BLANK # 범위 영역 폭탄

    # 중력 적용
    # 열 선택
    for col in range(n):
        idx = n-1
        for row in range(n-1,-1,-1):
            if grid[row][col] != BLANK:
                next_grid[idx][col] = grid[row][col]
                idx -= 1
    
    # 변경 사항 원본 적용
    for i in range(n):
        for j in range(n):
            grid[i][j] = next_grid[i][j]

for r in range(m):
    col = int(input())
    simulation(col-1)

for row in grid:
    print(*row)
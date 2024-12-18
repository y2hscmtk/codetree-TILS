'''
1. 폭발 구현
2. 중력 구현
'''
BLANK = 0

n = int(input())

grid = [list(map(int,input().split())) for _ in range(n)]

next_grid = [[0]*n for _ in range(n)]

r,c = map(int,input().split())

def in_range(x,y):
    if 0<=x<n and 0<=y<n:
        return True
    return False

def simulation(r,c):
    dsx = [0,0,-1,1]; dsy = [-1,1,0,0]
    # r,c 좌표에 적힌 숫자에서 십자 크기 영역 제거
    target = grid[r][c]
    grid[r][c] = 0 # 시작 위치 제거

    for t in range(target):
        for dx,dy in zip(dsx,dsy):
            nx = r + t*dx
            ny = c + t*dy
            if in_range(nx,ny):
                grid[nx][ny] = 0

    # 제거한 영역에 중력 적용
    # 첫번째 열부터 시작
    for col in range(n):
        idx = n-1
        for row in range(n-1,-1,-1):
            if grid[row][col] != BLANK: # 공백이 아닌 영역 발견시
                next_grid[idx][col] = grid[row][col]
                idx-=1

    # grid 갱신
    for i in range(n):
        for j in range(n):
            grid[i][j] = next_grid[i][j]

simulation(r-1,c-1)

for row in grid:
    print(*row)
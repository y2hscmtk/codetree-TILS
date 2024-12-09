n,r,c = map(int,input().split())

data = [list(map(int,input().split())) for _ in range(n)]

def in_range(x,y):
    if 0<=x<n and 0<=y<n:
        return True
    return False

def move(x,y):
    dsx = [-1,1,0,0]; dsy = [0,0,-1,1] # 상하좌우
    while True:
        print(data[x][y], end = ' ')
        find = False
        for dx,dy in zip(dsx,dsy):
            nx = x + dx; ny = y + dy
            if in_range(nx,ny) and data[x][y] < data[nx][ny]:
                x = nx; y = ny
                find = True
                break # 상하좌우 중 조건을 만족하는 위치 발견시 다른 방향 탐색 필요 없음
        if not find:
            break

move(r-1,c-1)
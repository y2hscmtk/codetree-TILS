'''
한 행이 이동한 후 바람이 전파될지 여부를 결정한다.
바람은 위,아래 행으로 전파되며 기존 바람의 반대방향으로 전파된다.
전파가 되는 조건은 현재 행과 다음 행을 비교했을 때 같은 열에 하나라도 같은 숫자가 존재한다면 전파됨
'''
mapper = {'L':0,'R':1}
n,m,q = map(int,input().split())

grid = [list(map(int,input().split())) for _ in  range(n)]

next_grid = [[0]*m for _ in range(n)]

def wind(r,d):
    if d == 0:
        for i in range(m-1,0,-1):
            next_grid[r][i] = grid[r][i-1]
        next_grid[r][0] = grid[r][m-1]
    else:
        for i in range(m-1):
            next_grid[r][i] = grid[r][i+1]            
        next_grid[r][m-1] = grid[r][0]

# 바람 확산
def spread(r,w,d):
    wind(r,d) # 현재 행 바람 전파
    nr = r + w
    if 0<=nr<n:
        for i in range(m):
            if next_grid[r][i] == next_grid[nr][i]:
                spread(nr,w,(d+1)%2)
                break

def start_wind(r,d):
    wind(r,d) # 현재 행 바람 전파

    # 위로 전파 된 바람이 다시 아래로 전파되는 일이 존재하는가 - x 예제에서 확인됨
    for w in (-1,+1): # 위, 아래 전파 확인
        nr = r + w
        if 0<=nr<n:
            for i in range(m):
                if next_grid[r][i] == next_grid[nr][i]:
                    spread(nr,w,(d+1)%2)
                    break

def simulation(r, d):
    # next_grid 초기화
    for i in range(n):
        for j in range(m):
            next_grid[i][j] = grid[i][j]

    # 재귀 함수 형태로 작성
    # 1. r행으로 바람이 분다.
    # 2. r행과 인접한 위,아래로 바람이 전파 되는지 확인
    # 바람이 전파될 여지가 있다면 재귀호출 - 시작 행, 진행 방향
    start_wind(r,d)

    # grid에 next_grid 할당
    for i in range(n):
        for j in range(m):
            grid[i][j] = next_grid[i][j]

for _ in range(q):
    r,d = input().split()
    simulation(int(r)-1,mapper[d])


for row in grid:
    print(*row)
n = int(input())

grid = [list(map(int,input().split())) for _ in range(n)]

r,c,m1,m2,m3,m4,d = map(int,input().split())

# d 
# 0 : 반시계
# 1 : 시계 방향

r,c = r-1,c-1

if d == 0:
    # 방향 1
    # r-1,c+1
    first = grid[r-m1][c+m1]
    i = 0
    for i in range(m1):
        grid[r-m1+i][c+m1-i] = grid[r-m1+i+1][c+m1-i-1]

    # 방향 2
    # r-1,c-1
    x,y = r-m1, c+m1
    second = grid[x-m2][y-m2]
    j = 0
    for i in range(m2-1):
        grid[x-m2+i][y-m2+i] = grid[x-m2+i+1][y-m2+i+1]
        j+=1
    grid[x-m2+j][y-m2+j] = first

    # 방향 3
    # r+1,c-1
    x,y = x-m2,y-m2
    third = grid[x+m3][y-m3]
    j = 0
    for i in range(m3-1):
        grid[x+m3-i][y-m3+i] = grid[x+m3-i-1][y-m3+i+1]
        j+=1
    grid[x+m3-j][y-m3+j] = second

    # 방향 4
    # r+1, c+1
    x,y = x+m3,y-m3
    four = grid[x+m4][y+m4]
    j = 0
    for i in range(m4-1):
        grid[x+m4-i][y+m4-i] = grid[x+m4-i-1][y+m4-i-1]
        j+=1
    grid[x+m4-j][y+m4-j] = third

else:
    # 방향 1
    # r+1, c-1s
    first = grid[r][c]
    i = 0
    for i in range(m1):
        grid[r-i][c+i] = grid[r-i-1][c+i+1]

    # 방향 2
    # r+1,c+1
    x,y = r-m1,c+m1
    second = grid[x-m2][y-m2]
    j = 0
    for i in range(m2-1):
        grid[x-i][y-i] = grid[x-i-1][y-i-1]
        j+=1
    grid[x-j][y-j] = second

    # 방향 3
    # r-1,c+1
    x,y = x-m2,y-m2
    third = grid[x+m3][y-m3]
    j = 0
    for i in range(m3):
        grid[x+i][y-i] = grid[x+i+1][y-i-1]

    # 방향 4
    # r-1, c-1
    x,y = x+m3,y-m3
    j = 0
    for i in range(m4-1):
        grid[x+i][y+i] = grid[x+i+1][y+i+1]
        j+=1
    grid[x+j][y+j] = first
    
    
for row in grid:
    print(*row)
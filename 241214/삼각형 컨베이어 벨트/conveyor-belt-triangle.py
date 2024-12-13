def move():
    first = grid[0][n-1]
    for i in range(n-1,0,-1):
        grid[0][i] = grid[0][i-1]
    second = grid[1][n-1]
    for i in range(n-1,0,-1):
        grid[1][i] = grid[1][i-1]
    grid[1][0] = first
    third = grid[2][n-1]
    for i in range(n-1,0,-1):
        grid[2][i] = grid[2][i-1]
    grid[2][0] = second
    grid[0][0] = third

n,t = map(int,input().split())

grid = [list(map(int,input().split())) for _ in range(3)]

for _ in range(t):
    move()

for row in grid:
    print(*row)
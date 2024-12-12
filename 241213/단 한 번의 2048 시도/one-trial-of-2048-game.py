'''
1. 중력을 적용할 방향 생각
2. 중력 적용시 바닥에서부터 시작하여 '같은 수' 2개가 되면 합치는 과정 수행 - 다른 수를 만나면 삽입, 같은 수를 만나면 삽입
3. 중력 적용 이후 grid 업데이트 필요
'''
grid = [list(map(int,input().split())) for _ in range(4)]

d = input() # 이동할 방향

new_grid = [[0]*4 for _ in range(4)]

def set_grid():
    for i in range(4):
        for j in range(4):
            grid[i][j] = new_grid[i][j]

# 오른쪽으로 미는 경우
def turn_right():
    for i in range(4):
        last = -1; temp = []
        for j in range(3,-1,-1):
            num = grid[i][j]
            if num == 0:
                continue
            if num != last:
                temp.append(num)
                last = num
            else: # num == last 같은 수 라면
                temp[-1] = 2*num
                last = -1
        # 중력 적용
        idx = 0
        for j in range(3,-1,-1):
            if idx < len(temp):
                new_grid[i][j] = temp[idx]
                idx += 1

# 왼쪽으로 미는 경우
def turn_left():
    for i in range(4):
        last = -1; temp = []
        for j in range(4):
            num = grid[i][j]
            if num == 0:
                continue
            if num != last:
                temp.append(num)
                last = num
            else: # num == last 같은 수 라면
                temp[-1] = 2*num
                last = -1
        # 중력 적용
        idx = 0
        for j in range(4):
            if idx < len(temp):
                new_grid[i][j] = temp[idx]
                idx += 1


# 아래로 미는 경우
def turn_down(): 
    for i in range(4):
        last = -1; temp = []
        for j in range(3,-1,-1):
            num = grid[j][i]
            if num == 0:
                continue
            if num != last:
                temp.append(num)
                last = num
            else: # num == last 같은 수 라면
                temp[-1] = 2*num
                last = -1
        # 중력 적용
        idx = 0
        for j in range(3,-1,-1):
            if idx < len(temp):
                new_grid[j][i] = temp[idx]
                idx += 1

# 위로 미는 경우
def turn_top():
    for i in range(4):
        last = -1; temp = []
        for j in range(4):
            num = grid[j][i]
            if num == 0:
                continue
            if num != last:
                temp.append(num)
                last = num
            else: # num == last 같은 수 라면
                temp[-1] = 2*num
                last = -1
        # 중력 적용
        idx = 0
        for j in range(4):
            if idx < len(temp):
                new_grid[j][i] = temp[idx]
                idx += 1

if d == 'U':
    turn_top()
elif d == 'D':
    turn_down()
elif d == 'L':
    turn_left()
elif d == 'R':
    turn_right()

set_grid()

# 정답 출력
for row in grid:
    print(*row)
'''
‘L', ‘R’, ‘U’, 'D’ 
왼쪽, 오른쪽, 위, 아래 방향
주사위의 초기 인덱스를 적어두고 각 방햫으로 굴릴때 주시위의 각 값이 어떻게 바뀌는지 정의
주사위 - 객체화
'''
dx = [0,0,-1,1]
dy = [-1,1,0,0]
mapper = {'L':0,'R':1,'U':2,'D':3}

n,m,r,c = map(int,input().split()) # 격자 크기, 굴릴 횟수, 초기위치
x,y = r-1,c-1

command = list(input().split())

board = [[0]*n for _ in range(n)] # 게임판
board[x][y] = 6 # 초기 값 지정

'''
  1       5
4 2 3   4 1 3
  6       2 
  5       6
'''
dice = [5,1,2,6,4,3]
# 왼쪽으로 굴리기
def turn_left():
    new_dice = [dice[0],dice[5],dice[2],dice[4],dice[1],dice[3]]
    return new_dice

# 오른쪽으로 굴리기
def turn_right():
    new_dice = [dice[0],dice[4],dice[2],dice[5],dice[3],dice[1]]
    return new_dice

# 위로 굴리기
def turn_top():
    new_dice = [dice[1],dice[2],dice[3],dice[0],dice[4],dice[5]]
    return new_dice

# 아래로 굴리기
def turn_bottom():
    new_dice = [dice[3],dice[0],dice[1],dice[2],dice[4],dice[5]]
    return new_dice

def in_range(x,y):
    if 0<=x<n and 0<=y<n:
        return True
    return False

def simulation(d):
    global x,y,dice # 주사위 위치 
    # d 방향으로 주사위 이동
    nx,ny = x + dx[d], y + dy[d]
    if not in_range(nx,ny):
        return # 격자 밖으로 벗어나는 경우라면 그 다음 과정을 수행한다.
    # 1. 주사위 굴리기
    if d == 0: # 왼쪽
        dice = turn_left()
    elif d == 1: # 오른쪽
        dice = turn_right()
    elif d == 2: # 위쪽
        dice = turn_top()
    elif d == 3 : # 아래쪽
        dice = turn_bottom()

    # 2. 바닥면 게임판에 적기
    board[nx][ny] = dice[3]
    x,y = nx,ny

def make_sum():
    result = 0
    for row in board:
        result += sum(row)
    return result

for c in command:
    simulation(mapper[c])

print(make_sum())

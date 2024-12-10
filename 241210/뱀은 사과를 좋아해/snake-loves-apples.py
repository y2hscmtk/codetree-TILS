from collections import deque
import sys
'''
위, 아래, 오른쪽, 왼쪽
‘U', ‘D’, ‘R’, 'L’
'''
conv = {'U':0, 'D':1, 'R':2, 'L':3}
dx = [-1,1,0,0]; dy = [0,0,1,-1]
n,m,k = map(int,input().split())
board = [[0]*n for _ in range(n)]
x,y = 0,0 # 뱀의 초기 위치
time = 0 # 게임 진행 시간
snake = deque()
snake.append((0,0))
game_progress = True # 게임 진행 여부

# 사과 위치 입력받기
apple_pos = []
for _ in range(m):
    x,y = map(int,input().split())
    board[x-1][y-1] = 1 # 사과의 위치 기록
# 명령 입력받기
command = []
for _ in range(k):
    c, t = input().split()
    command.append((conv[c],int(t)))

def in_range(x,y):
    if 0<=x<n and 0<=y<n:
        return True
    return False

def simulation(d,t):
    global x,y,time,game_progress
    for _ in range(t): # d방향으로 t번 이동
        x,y = snake[-1] # 머리 좌표
        nx = x + dx[d]
        ny = y + dy[d]
        if not in_range(nx,ny): # 격자를 벗어나면 게임 종료
            time += 1 
            game_progress = False
            return
        # 이동하려는 칸에 사과가 존재한다면
        if board[nx][ny] == 1:
            board[nx][ny] = 0 # 사과 제거
            snake.append((nx,ny)) # 머리 추가
        else: # 사과가 존재하지 않는 경우
            snake.popleft() # 꼬리 제거
            if (nx,ny) in snake: # 다음에 머리가 이동할 칸에 몸통이 있는지 확인
                time += 1
                game_progress = False
                return
            # 몸통과 겹치지 않는다면 이동
            snake.append((nx,ny))
        time += 1 # 움직이는데 1초 소요

            
# 게임이 진행되는 동안 차례로 명령 수행
for d,t in command:
    if game_progress:
        simulation(d,t)
    else:
        break
print(time)
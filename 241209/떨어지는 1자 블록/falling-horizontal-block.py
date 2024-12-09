n,m,k = map(int,input().split())

board = [list(map(int,input().split())) for _ in range(n)]

# k-1의 위치에서 가로 길이 m인블록이 떨어지는 상황
# k-1에서부터 k-1 + m-1 까지의 열 검사
def find_row():
    for i in range(n): # 가장 윗줄부터 가장 아래줄까지 검사
        for j in range(k-1,k-1+m):
            if board[i][j] == 1: # 해당 줄에 블록이 존재한다면 블록은 떨어질 수 없음
                return i-1 # 블록이 떨어져 최종적으로 위치하게 될것
    return -1

row = find_row()
# 블록이 1칸이라도 떨어졌는지 확인
if row >= 0:
    for j in range(k-1,k-1+m):
        board[row][j] = 1 # 블록 끼워넣기

for row in board:
    print(*row)
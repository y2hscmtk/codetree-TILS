dx = [0,0,-1,1]
dy = [-1,1,0,0]

n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]

'''
1. 폭탄이 터질 위치 선정
2. 폭탄 터뜨리기 시뮬레이션
    2.1. 배열 복사
    2.2. 복사된 배열에서 폭탄 터뜨리기 - 인덱스 검사, 터질 영역 0으로 교체, 적힌 숫자 크기만큼 폭탄 떠뜨리기
    2.3. 중력 적용
    2.4. 2개의 칸으로 쌍이 이루어진 동일한 숫자 쌍 찾기
'''
result = 0
def bomb_simulation(x,y):
    global result
    # 1. 배열 복사
    cboard = [b[:] for b in board]
    # 2. (x,y)좌표를 기준으로 폭탄 떠뜨리기
    p = cboard[x][y]
    cboard[x][y] = 0 
    for np in range(p): # 1 : 0, 2: 0,1, 3: 0,1,2
        for i in range(4):
            nx = x + np*dx[i]; ny = y + np*dy[i]
            if 0<=nx<n and 0<=ny<n:
                cboard[nx][ny] = 0 # 폭탄 떠뜨리기
    # 3. 중력 적용
    for j in range(n): # 가장 왼쪽 줄부터 시작
        number = [] # 0을 제외한 숫자만 저장
        for i in range(n-1,-1,-1):
            if cboard[i][j] != 0:
                number.append(cboard[i][j])
        number += [0]*(n-len(number)) # 나머지는 빈공간으로 설정
        # 숫자 채워넣기 - 중력 적용
        for i in range(n-1,-1,-1):
            cboard[i][j] = number[(n-1)-i]
    # 4. 동일한 순서쌍 파악
    # 4.1. 가로 순서쌍 파악
    t_count = 0 
    for i in range(n):
        num = cboard[i][0]
        count = 0
        for j in range(n):
            if cboard[i][j] == num:
                count += 1
            else:
                if count == 2 and num != 0:
                    t_count += 1 # 순서쌍 개수 
                num = cboard[i][j]
                count = 1
        if count == 2 and num != 0:
            t_count += 1
    
    # 4.2. 세로 순서쌍 파악
    for i in range(n):
        num = cboard[0][i]
        count = 0
        for j in range(n):
            if cboard[j][i] == num:
                count += 1
            else:
                if count == 2 and num != 0:
                    t_count += 1 # 순서쌍 개수 
                num = cboard[j][i]
                count = 1
        if count == 2 and num != 0:
            t_count += 1
    
    result = max(result,t_count)
    
for i in range(n):
    for j in range(n):
        bomb_simulation(i,j)

print(result)
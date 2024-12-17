'''

(0,0) , (0,1)   |  (-1,0)           |          (-1,0)   |  (0,-1) , (0, 0)
(1,0)           |  (0, 0) , (0, 1)  | (0,-1) , (0, 0)   |           (1, 0)

                          |   (-1,0)
(0,-1) , (0, 0) , (0, 1)  |   (0, 0)
                          |   (1, 0)

1. 모든 모양에 대해 dx,dy로 정의
2. 완전 탐색 수행하며 범위를 벗어나지 않는지 검사
3. 조건을 만족한다면 합 결과 갱신
'''

n, m = map(int,input().split())

data = [list(map(int,input().split())) for _ in range(n)]

max_sum = 0 # 최대합

dsx = [[1,0],[-1,0],[-1,0],[0,1],[0,0],[-1,1]]
dsy = [[0,1],[0,1],[0,-1],[-1,0],[-1,1],[0,0]]

def in_range(x,y):
    if 0<=x<n and 0<=y<m:
        return True
    return False

def update_max_sum(x,y):
    temp_max_sum = 0
    find = False
    for t in range(6):
        temp = data[x][y]
        error = False
        for dx,dy in zip(dsx[t],dsy[t]):
            nx,ny = x + dx, y + dy
            if not in_range(nx,ny):
                error = True
                break
            temp += data[nx][ny]
        if not error:
            find = True
            temp_max_sum = max(temp_max_sum,temp)
    if find:
        return temp_max_sum
    return -1

def find_max_sum():
    global max_sum
    for i in range(n):
        for j in range(m):
            result = update_max_sum(i,j)
            if result != -1:
                max_sum = max(max_sum,result)

find_max_sum()
print(max_sum)

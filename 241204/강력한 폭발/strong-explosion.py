'''
1이 적힌 위치에 폭탄 설치 가능
3가지 유형의 폭탄 설치 가능
가장 많은 영역을 초토화 시킬 수 있도록 프로그램 작성
'''
n = int(input())

graph = []; bomb_position = []
c = 0 # 폭탄 설치가 가능한 영역의 수
visited = [[False]*n for _ in range(n)] # 각 영역에 폭탄이 터졌는지 안터졌는지 확인용
for i in range(n):
    row = list(map(int,input().split()))
    for j in range(n):
        if row[j] == 1: # 폭탄을 놓을 수 있는 위치라면 기록
            bomb_position.append((i,j))
            visited[i][j] = True # 폭탄 설치 가능 영역은 항상 터짐
            c+=1
    graph.append(row)

bomb_type = [] # 각 위치에 설치할 폭탄의 유형

result = 0; count = c # 폭탄 설치 가능 위치만큼
# 어떤 폭탄을 설치할지 선정
def dfs(cnt):
    global result,count,visited
    if cnt == c: # c개 모두 설치시
        # 현재까지 폭파된 영역 갱신
        result = max(result,count)
        return
    
    # 1,2,3 3가지 유형 중 1개의 폭탄 설치
    for i in range(1,4):
        bomb_type.append(i)
        backup = [v[:] for v in visited]
        # 폭탄 유형에 맞춰 폭탄 터뜨리기
        destroy_count = destroy_bomb(cnt)
        count += destroy_count
        dfs(cnt+1)
        count -= destroy_count
        visited = [b[:] for b in backup] # 백트래킹
        bomb_type.pop()

# 폭탄 터뜨리기
# 폭탄 유형1, 2, 3
dx = [[],[-1,-2,1,2], [-1,1,0,0], [-1,-1,1,1]]
dy = [[],[0,0,0,0], [0,0,-1,1], [-1,1,-1,1]]
def destroy_bomb(cnt):
    type = bomb_type[cnt]
    x, y = bomb_position[cnt]
    temp_count = 0
    for i in range(len(dx[type])):
        nx,ny = x + dx[type][i], y + dy[type][i]
        # 영역을 벗어나지 않으면서 아직 터지지 않은 공간인 경우
        if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
            temp_count += 1
            visited[nx][ny] = True
    return temp_count

dfs(0)
print(result)
'''
현재 칸의 이동 방향에서 
정면에 벽이 존재한다면 -> 왼쪽으로 이동 방향 변경
오른쪽 위 칸에 벽이 존재한다면 -> 이동방향 변경x
오른쪽 위 칸에 벽이 존재하지 않는다면 -> 오른쪽으로 이동 방향 변경
'''
n = int(input())
x,y = map(int,input().split())
x-=1; y-=1

graph = [list(input()) for _ in range(n)]
visited = [[False]*n for _ in range(n)]

def in_range(x,y):
    if 0<=x<n and 0<=y<n:
        return True
    return False

def move(x,y):
    dx = [0,1,0,-1]; dy = [1,0,-1,0]; d = 0; time = 0
    while True:
        nx = x + dx[d]
        ny = y + dy[d]
        if in_range(nx,ny):
            if graph[nx][ny] == '#': # 진행 방향 앞에 벽이 있다면
                d = (d-1)%4 # 왼쪽으로 방향 변경
                x = x + dx[d]; y = y + dy[d]
                time += 1
            else:
                nnx = nx + dx[(d+1)%4]; nny = ny + dy[(d+1)%4]
                if graph[nnx][nny] == '#': # 진행 방향이 바뀌지 않는 경우
                    x = nx; y = ny
                    time += 1
                else: # 돌아가야 되는 경우
                    time += 2 # 돌아서 아래로 이동
                    d = (d+1)%4
                    x = nnx; y = nny
                # 다음에 이동할 위치가 한번 방문한적 있는 경우 - 탈출 불가
                if visited[x][y]:
                    print(-1)
                    break
                visited[x][y] = True # 이동할 위치 방문 처리
            if not in_range(x,y):
                print(time)
                break
        else:
            print(time+1)
            break
    
move(x,y)
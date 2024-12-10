'''
구현,시뮬레이션
'''
n,m,r,c = map(int,input().split())

visited = [[False]*n for _ in range(n)] # 격자판 생성

def simulation():
    dsx = [0,0,-1,1]; dsy = [-1,1,0,0]
    count = 1 # 폭탄의 개수 카운팅
    time = 0
    visited[r-1][c-1] = True
    bomb_ps = [(r-1,c-1)]
    while True:
        time += 1
        if time == m+1:
            return count
        new_bomb_ps = []
        for x,y in bomb_ps:
            for dx,dy in zip(dsx,dsy):
                nx = x + time*dx
                ny = y + time*dy
                if 0<=nx<n and 0<=ny<n and not visited[nx][ny]: # 폭탄이 놓인적 없는 위치로만 폭탄 이동 가능
                    visited[nx][ny] = True
                    new_bomb_ps.append((nx,ny))
                    count+=1
        new_bomb_ps.append((x,y)) # 현재 위치도 또한번 폭탄이 터지는 위치에 해당
        bomb_ps = new_bomb_ps
        

print(simulation())
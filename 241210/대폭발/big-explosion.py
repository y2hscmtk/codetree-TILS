'''
구현,시뮬레이션
'''
from collections import deque
n,m,r,c = map(int,input().split())

graph = [[0]*n for _ in range(n)] # 격자판 생성
# 0인 좌표는 폭탄이 존재하지 않음
queue = deque()
queue.append((r-1,c-1))

def simulation():
    dsx = [0,0,-1,1]; dsy = [-1,1,0,0]
    count = 1 # 폭탄의 개수 카운팅
    while queue:
        x,y = queue.popleft()
        graph[x][y] += 1 # 현재 폭탄이 있던 위치에서 1초가 지남
        time = graph[x][y]
        if time == m+1: # 목표 시간 도달시 종료
            return count
        for dx,dy in zip(dsx,dsy):
            nx = x + time*dx
            ny = y + time*dy
            if 0<=nx<n and 0<=ny<n and graph[nx][ny] == 0: # 폭탄이 놓인적 없는 위치로만 폭탄 이동 가능
                graph[nx][ny] = graph[x][y]
                queue.append((nx,ny))
                count+=1
        queue.append((x,y)) # 현재 위치도 또한번 폭탄이 터지는 위치에 해당

print(simulation())
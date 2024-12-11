'''
구현, 시뮬레이션
'''
n,m,t = map(int,input().split())
'''
 ‘U', ‘D’, ‘R’, 'L’ 
 위,아래,오른쪽,왼쪽
'''
dx = [-1,1,0,0]
dy = [0,0,1,-1]
mapper = {'U':0,'D':1,'R':2,'L':3}

beads = []

# 구슬 정보 입력받기
for i in range(m):
    r,c,d,w = input().split()
    # 구슬 정보 저장
    beads.append([int(r)-1,int(c)-1,mapper[d],int(w),i]) # 가장 마지막 요소는 번호

def in_range(x,y):
    if 0<=x<n and 0<=y<n:
        return True
    return False

def reverse_dir(d):
    if d == 0:
        d = 1
    elif d == 1:
        d = 0
    elif d == 2:
        d = 3
    elif d == 3:
        d = 2
    return d

# 1. 구슬이 움직인다.
def move_beads():
    global beads
    new_beads = [] # 새로 변화된 구슬의 위치
    # 모든 구슬에 대하여
    for x,y,d,w,num in beads:
        nx = x + dx[d]
        ny = y + dy[d]
        # 영역을 벗어나는 경우라면 방향은 정 반대가 된다. (위치는 변화하지 않음)
        if not in_range(nx,ny):
            d = reverse_dir(d)
            new_beads.append([x,y,d,w,num]) 
            continue # 다른 구슬 탐색 - 현재 구슬 움직임 종료
        # 영역을 벗어나지 않는다면 새로운 위치로 구슬 삽입
        new_beads.append([nx,ny,d,w,num])
    # 구슬 위치 정보 업데이트
    beads = new_beads


# 2. 같은 위치에 있는 구슬끼리 합쳐진다.
def merge_beads():
    global beads
    is_checked = [False]*len(beads) # 각 구슬을 확인했는지 여부
    new_beads = []
    # 모든 구슬에 대하여
    for i in range(len(beads)):
        # i 번째 이후 구슬들에 대하여 i번째 구슬과 위치가 겹치는지 확인
        x_i,y_i,d_i,w_i,num_i = beads[i]
        if is_checked[i]: # 앞서 확인 처리된 구슬이라면 넘어가기
            continue
        for j in range(i+1,len(beads)):
            x_j,y_j,d_j,w_j,num_j = beads[j]
            if (x_i,y_i) == (x_j,y_j): # 확인 검사 필요?
                is_checked[j] = True # 확인 처리
                # 방향은 합쳐진 구슬들 중 가장 큰 번호가 매겨져있는 구슬의 방향을 따르게 되고
                # 번호는 마찬가지로 충돌이 일어난 구슬들 중 가장 큰 번호를 갖게 된다.
                if num_i < num_j:
                    d_i = d_j 
                    num_i = num_j
                # 구슬의 무게는 해당 위치에 모인 모든 구슬의 합으로 결
                w_i += w_j
        new_beads.append([x_i,y_i,d_i,w_i,num_i])
    beads = new_beads
                   

# t초 동안 시뮬레이션 수행
for i in range(t):
    # 1. 구슬이 움직인다.
    move_beads()
    # 2. 같은 위치에 존재하는 구슬끼리 합쳐진다.
    merge_beads()

# 남아있는 구슬의 수와 가장 무거운 구슬의 무게 출력
max_weight = 1
for x,y,d,w,num in beads:
    max_weight = max(max_weight,w)

print(len(beads),max_weight)
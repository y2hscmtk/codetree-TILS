'''
겪자 안의 모든 값이 양수인 최대 크기의 양수 직사각형 찾기
최대 크기 -> 직사각형 자체의 크기를 의미
'''

n,m = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(n)]


def check(x,y,heigth,length):
    for i in range(x,x+heigth):
        for j in range(y,y+length):
            if graph[i][j] < 0:
                return False
    return True


result = -1
# 가능한 최대 세로 길이
for i in range(1,n+1):
    # 가능한 최대 가로 길이
    for j in range(1,m+1):
        find = False
        # 탐색 시작 좌표 설정
        for x in range(n-i+1):
            if find:
                break
            for y in range(m-j+1):
                if check(x,y,i,j):
                    result = max(result,i*j)
                    find = True
                    break

print(result)
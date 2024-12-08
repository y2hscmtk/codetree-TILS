n,m = map(int,input().split())

data = []

for _ in range(n):
    data.append(list(map(int,input().split())))

min_dist = float('inf')

# 점 2개 고르기 - 어차피 점 2개 골라서 거리 구해야됨
for i in range(n):
    x1,y1 = data[i]
    for j in range(i+1,n):
        x2,y2 = data[j]
        dist = (x1-x2)**2 + (y1-y2)**2
        min_dist = min(min_dist,dist)

print(min_dist)
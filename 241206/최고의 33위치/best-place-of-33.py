n = int(input())
data = [list(map(int,input().split())) for _ in range(n)]

def count_coin(i,j):
    temp = 0
    for x in range(i,i+3):
        for y in range(j,j+3):
            if data[x][y] == 1:
                temp+=1
    return temp
                
result = 0
for i in range(n-3+1):
    for j in range(n-3+1):
        result = max(result,count_coin(i,j))
        
print(result)
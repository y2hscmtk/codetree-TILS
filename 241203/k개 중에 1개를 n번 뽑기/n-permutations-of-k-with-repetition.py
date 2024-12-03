def dfs(depth):
    if depth == N:
        print(*result)
        return
    
    for i in range(1,K+1):
        result.append(i)
        dfs(depth+1)
        result.pop()

K,N = map(int,input().split())
result = []
dfs(0)
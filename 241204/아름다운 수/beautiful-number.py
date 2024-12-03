
def check():
    last = number[0]
    count = 1
    for i in range(1,n):
        if number[i] == last:
            count += 1
        else: # 다른 수가 나왔다면
            if count % last != 0:
                return False
            last = number[i]
            count = 1
    # 마지막 수까지 도달한 이후 count 검사
    if count % last != 0:
        return False
    return True

result = 0
def dfs(depth):
    global result
    if depth == n:
        # 아름다운 수인지 검사
        if check():
            result += 1
        return
    for i in range(1,5): # 1이상 4이하의 숫자로 구성
        number.append(i)
        dfs(depth+1)
        number.pop()


n = int(input())
number = []
dfs(0)
print(result)
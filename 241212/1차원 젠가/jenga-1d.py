'''
1. 빈 배열을 만든다.
2. 원본 배열을 돌면서 조건에 맞춰 빈 배열의 앞부터 값을 삽입한다.
3. 빈 배열을 원본 배열에 할당한다.
'''
BLANK = 0
n = int(input())
block = []
for _ in range(n):
    block.append(int(input()))

def remove_block(s,e):
    global block
    temp = [] # 임시 배열
    # 1. 블록 제거
    for i in range(s-1,e):
        block[i] = BLANK
    # 2. 중력 적용
    for b in block:
        if b != BLANK:
            temp.append(b)
    # 3. 적용된 블록 원본 배열에 할당
    block = temp

# 제거할 블록 순서
for _ in range(2):
    remove_block(*map(int,input().split()))

# 남아있는 블록 정보 출력
print(len(block))
for b in block:
    print(b)
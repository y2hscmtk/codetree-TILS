'''
오후 7시 22분
같은 알파벳에는 같은 숫자가 들어가야 됨에 유의
식의 길이만큼 돌면서 사용한 알파벳 딕셔너리에 기록 및 사용한 알파벳 카운팅
각 알파벳에 대해서 백트래킹 수행 1~4까지의 숫자 기록 -> 모두 기록시 기존식에 대입하여 계산
식 계산 함수 구현 필요
'''
dict = {} # 사용한 알파벳 딕셔너리
data = input()
count = 0 # 사용된 알파벳의 총 수
array = [] # 사용한 알파벳
result = 0 # 식의 결과 
for a in data:
    if a not in "+-*": # 알파벳이라면
        if a not in dict: # 처음 등장한 알파벳이라면
            array.append([a,0]) # 특정 알파벳
            count += 1
            dict[a] = 0 # 0으로 기록


# 숫자 초기화
def dict_init(): 
    for a in dict:
        dict[a] = 0

# 딕셔너리 값 주입
def dict_update():
    for i in range(count):
        dict[array[i][0]] = array[i][1]


def calc(n1,e,n2):
    if e == '+':
        return n1+n2
    elif e == '-':
        return n1-n2
    elif e == '*':
        return n1*n2

# 수식 계산
def find_result():
    global result
    dict_update() # 알파벳 숫자 주입

    temp = dict[data[0]] # 수식 결과
    
    for i in range(0,len(data)-2,2):
        temp = calc(temp,data[i+1],dict[data[i+2]])

    result = max(result,temp)

    dict_init() # 알파벳 숫자 초기화



def dfs(s,cnt):
    if cnt == count: # 모든 숫자를 채워 넣었다면
        find_result() # 수식 계산
        return
    
    # i번째 알파벳을 어떤 숫자로 변환할지 결정
    for i in range(s,count):
        # 1~4까지 숫자 대입 가능
        for num in range(1,5):
            array[i][1] = num
            dfs(i+1,cnt+1)
            array[i][1] = 0 # 백트래킹


dfs(0,0)
print(result)
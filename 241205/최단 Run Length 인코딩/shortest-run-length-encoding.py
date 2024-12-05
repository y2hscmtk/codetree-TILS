'''
1칸부터, n칸만큼 밀 수 있음
새롭게 생성된 단어에서 Run-Length Encoding 수행
'''
data = list(input())
n = len(data)

result = n # 최소 길이
# 몇칸을 밀 것인지 결정
for j in range(1,n):
    data = [data[-1]] + data[:-1]
    # 데이터 압축 수행
    count = 1
    alphabet = data[0]
    for i in range(1,n):
        if alphabet != data[i]:
            alphabet = data[i]
            count += 1
    if count == 1:
        result = min(result,3)
    else:
        result = min(result,count*2)
        
print(result)
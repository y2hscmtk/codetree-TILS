'''
1칸부터, n칸만큼 밀 수 있음
새롭게 생성된 단어에서 Run-Length Encoding 수행
'''
data = list(input())
n = len(data)

data = data*2

min_count = 2*n
for i in range(0,n):
    # 슬라이딩 윈도우
    a_count = 1
    alphabet = data[i]
    result = data[i]
    for j in range(i+1,i+n):
        if alphabet != data[j]:
            result += str(a_count) + data[j]
            alphabet = data[j]
            a_count = 1
        else:
            a_count += 1
    if result[-1] not in '1234567890':
        result += str(a_count)
    min_count = min(min_count,len(result))
print(min_count)    
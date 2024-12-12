n,t = map(int,input().split())

array = [list(map(int,input().split())) for _ in range(2)]

new_array = array[0] + array[1]

# 한줄이라고 생각
def simulation():
    global new_array
    new_array = [new_array[-1]] + new_array[:-1]

for _ in range(t):
    simulation()


for i in range(n):
    print(new_array[i], end=' ')
print()
for i in range(n,2*n):
    print(new_array[i], end=' ')
def star1(depth):
    if depth == 0:
        return
    for i in range(depth):
        print("*", end = ' ')
    print()
    star1(depth-1)

def star2(depth):
    if depth == n+1:
        return
    for i in range(depth):
        print("*", end = ' ')
    print()
    star2(depth+1)

n = int(input())
star1(n)
star2(1)
    
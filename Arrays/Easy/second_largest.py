def second_largest(v):
    maxi1 = float('-inf')
    maxi2 = float('-inf')

    for x in v:
        if x > maxi1:
            maxi2 = maxi1
            maxi1 = x
        elif x > maxi2 :  
            maxi2 = x

    return maxi2

# Input
n = int(input())
v = list(map(int, input().split()))

print(second_largest(v))

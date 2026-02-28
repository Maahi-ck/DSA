def largest(v):
    maxi = float('-inf')
    for x in v:
        if x > maxi:
            maxi = x
    return maxi


n = int(input())
v = list(map(int, input().split()))

print(largest(v))

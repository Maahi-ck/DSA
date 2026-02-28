def check(v):
    n = len(v)
    for i in range(1, n):     ## 1 to n-1
        if v[i] < v[i - 1]:
            return False
        
    return True


n = int(input())
v = list(map(int, input().split()))

print(check(v))

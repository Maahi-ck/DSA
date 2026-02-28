def linear_search(v, ele):
    for x in v:
        if x == ele:
            return True
        
    return False


n = int(input())
v = list(map(int, input().split()))

ele = int(input())
print(linear_search(v, ele))

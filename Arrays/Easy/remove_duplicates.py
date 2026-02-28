def fun(v):
    n = len(v)

    ans = [  v[0]  ]
    for i in range(1, n): 
        if v[i] != v[i - 1]:
            ans.append(v[i])
            
    return ans


n = int(input())
v = list(map(int, input().split()))

result = fun(v)
print(result)

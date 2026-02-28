def union_(a, b):
    mpp = {}
    for x in a:
        mpp[x] = mpp.get(x, 0) + 1
        
    for x in b:
        mpp[x] = mpp.get(x, 0) + 1

    for key in mpp:
        print(key, end=" ")
    print()


def intersection(a, b):
    mpp = {}
    ans = {}
    
    for x in a:
        mpp[x] = mpp.get(x, 0) + 1

    for x in b:
        if x in mpp:
            ans[x] = ans.get(x, 0) + 1

    for key in ans:
        print(key, end=" ")
    print()


# Input
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

union_(a, b)
intersection(a, b)

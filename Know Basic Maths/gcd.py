# Time complexity: O(log(min(a, b)))

def gcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    if b > a:
        a, b = b, a
    return gcd(b, a % b)


a = 42
b = 48
print(gcd(a, b))

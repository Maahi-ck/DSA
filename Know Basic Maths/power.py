# Brute force
# Time complexity = O(b)
def power1(a, b):
    ans = 1
    for _ in range(b):
        ans *= a
    return ans


# Optimized (Binary Exponentiation)
# Time complexity = O(log(b))
def power2(a, b):
    ans = 1
    while b > 0:
        if b % 2 == 1:
            ans *= a
            b -= 1
        a *= a
        b //= 2
    return ans


a = 3
b = 5
print(power1(a, b))
print(power2(a, b))

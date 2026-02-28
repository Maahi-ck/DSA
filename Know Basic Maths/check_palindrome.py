def check1(s):
    n = len(s)
    rev = [' '] * n

    for i in range(n):
        rev[i] = s[n - i - 1]

    for i in range(n):
        if s[i] != rev[i]:
            return False
    return True


def check2(s):
    n = len(s)
    for i in range(n):
        if s[i] != s[n - i - 1]:
            return False
    return True


s = input("Enter a string\n")
print(check1(s))
print(check2(s))

# Time complexity: O(length of string) = O(n)

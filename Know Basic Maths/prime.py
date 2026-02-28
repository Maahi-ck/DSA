# Time complexity = O(sqrt(num))
def check(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


num = int(input("Enter a number\n"))
print(check(num))

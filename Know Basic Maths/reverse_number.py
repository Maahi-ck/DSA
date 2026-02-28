def reverse_number(num):
    ans = 0
    while num != 0:
        r = num % 10
        ans = ans * 10 + r
        num //= 10
    return ans


num = int(input("Enter a number\n"))
print(reverse_number(num))

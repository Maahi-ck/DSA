# Time complexity = O(number of digits) = O(log(num))
# A number num contains log(num) digits

def count_digits(num):
    ans = 0
    while num != 0:
        num //= 10
        ans += 1
    return ans


num = int(input("Enter a number\n"))
print(count_digits(num))

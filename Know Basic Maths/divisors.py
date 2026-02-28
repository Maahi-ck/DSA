def print_divisors(num):
    div = []

    i = 1
    while i * i <= num:
        if num % i == 0:
            div.append(i)
            if i * i != num:
                div.append(num // i)
        i += 1

    for d in div:
        print(d, end=" ")
    print()


num = int(input("Enter a number\n"))
print_divisors(num)

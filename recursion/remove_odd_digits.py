def remove_odd_digits(num):
    neg = 1
    if num < 0:
        neg = -1
        num = abs(num)
    lastdigit = int(num%10)
    if lastdigit == 0:
        if num >10:
            return (remove_odd_digits(int(num//10))*10) * neg
        else:
            return 0
    elif lastdigit % 2 != 0:
        return (remove_odd_digits(int(num//10))) * neg
    else:
        return (remove_odd_digits(int(num//10))*10 + lastdigit) * neg




def even_digits(num):
    minus = 1
    if '-' in str(num):
        minus = -1
        num = int(str(num)[1:])
    num, rem = divmod(num,10)
    if num != 0:
        if rem % 2 == 0:
            return minus * (10 * even_digits(num) + rem)
        else:
            return minus * (even_digits(num))
    else:
        if rem % 2 == 0:
            return minus * rem
        else:
            return 0

print(even_digits(8342116)) # 8426
print(even_digits(-163505))
print(even_digits(-2))
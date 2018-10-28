def star_string(num):
    if num < 0:
        raise ValueError()
    if num == 0:
        return '*'
    else:
        return '*'*(2**num - 2**(num-1)) + star_string(num-1)



def sum_up_to(num):
    if num < 0:
        raise ValueError('shit')
    if num == 0:
        return 0
    if num == 1:
        return 1
    else:
        return sum_up_to(num-1) + 1/num

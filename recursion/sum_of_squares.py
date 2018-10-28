def sum_of_squares(num):
    if num < 0:
        raise ValueError('Shit')
    if num == 0:
        return 0
    if num == 1:
        return 1**2
    else:
        return sum_of_squares(num-1) + num**2 

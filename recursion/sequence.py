def sequence(num):
    if num < 1:
        raise ValueError()
    if num == 1:
        print(1,end='')
    else:
        if num % 2 == 0:
            print('(' + str(num) + ' +', end=' ')
            sequence(num-1)
            print(')',end='')
        else:
            print('(', end='')
            sequence(num-1)
            print(' + ' + str(num) +')',end='')

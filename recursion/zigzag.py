def zigzag(num):
    if num <= 0:
        raise ValueError('Shit')
    if num == 1:
        print('*',end='')
    elif num == 2:
        print('**', end='')
    else:
        print('<',end='')
        zigzag(num-2)
        print('>',end='')

zigzag(1)
print()
zigzag(2)
print()
zigzag(3)
print()
zigzag(4)
print()
zigzag(5)
print()
zigzag(6)
print()
zigzag(7)
    
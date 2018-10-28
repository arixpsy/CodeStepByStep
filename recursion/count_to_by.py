def count_to_by(m, n):
    if n == 0:
        raise ValueError('Shit')
    if m <= 0:
        raise ValueError('Shit')
    else:
        if m - n <= 0:
            print(m,end='')
        else:
            count_to_by(m-n,n)
            print(', ' + str(m), end='')


count_to_by(10,2)
print()
count_to_by(25,4)
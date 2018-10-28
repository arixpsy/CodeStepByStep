def digit_sum(number):
    length = len(str(number))
    
    if length == 1:
        return number
    else:
        end = int(str(number)[-1])
        if number < 0 :
            if length == 2 and '-' in str(number):
                return number
            front = int(str(number)[1:-1])
            return -1 * (digit_sum(front) + end)
        else:
            front = int(str(number)[:-1])
            return digit_sum(front) + end





print(digit_sum(-1729)) # -1 vs 17
print(digit_sum(1729))
print(digit_sum(-7))

def digits_sorted(num):
    neg = 1
    print('Start',num, num%10)
    if num < 0:
        neg = -1
    if num % 10 == num*neg:
        return True
    else:
        print((neg*num%10) , ((num*neg)//10%10),'Next loop:', (neg*num//10))
        return (neg*num%10) >= (num*neg//10%10) and digits_sorted(neg*num//10)

print(digits_sorted(0))	#True
print('Expected Answer: True')
print()
print(digits_sorted(2345))	#True
print('Expected Answer: True')
print()
print(digits_sorted(-2345))	#True
print('Expected Answer: True')
print()
print(digits_sorted(22334455))	#True
print('Expected Answer: True')
print()
print(digits_sorted(-5))	#True
print('Expected Answer: True')
print()
print(digits_sorted(4321))	#False
print('Expected Answer: False')
print()
print(digits_sorted(24378))#False
print('Expected Answer: False')
print()
print(digits_sorted(21))	#False
print('Expected Answer: False')
print()
print(digits_sorted(-33331))	#False
print('Expected Answer: False')
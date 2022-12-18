inp = input('Enter three sides ')
numbers = inp.split(' ')
a = int(numbers[0])
b = int(numbers[1])
c = int(numbers[2])

sum1 = a + b
sum2 = b + c
sum3 = a + c

while(sum1>c | sum2>a | sum3 >b):
    print('no')
    break
else:
    print('yes')

#
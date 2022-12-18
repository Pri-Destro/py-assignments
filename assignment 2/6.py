a = int(input('enter first num '))
b = int(input('enter second num '))


count = 0
x = a ^ b
while(x):
    count += 1
    x &= (x - 1)

print(count)
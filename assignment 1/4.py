num = "25,25,25"
sum = 0

for i in num.split(','):
    sum += int(i)
print(sum)
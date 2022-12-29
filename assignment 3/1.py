string = str(input('enter your string - '))

for i in range(len(string)):
    char = string[i]
    if char!=' ':
        print(f'number of {string[i]} is - {string.count(char)}')
        
    
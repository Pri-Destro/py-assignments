string  = 'Python is a case sensitive language'

length = len(string)           #a

rev_str = string[::-1]         #b

sliced_str = string[10:]       #c

new_str1 = string.replace('a case sensitive language','object oriented')     #d

for i in range(length):             #e
    if string[i] == 'a':            
        print(i)

new_str2 = string.replace(' ','')       #f




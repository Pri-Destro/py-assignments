dict = {}
rev_dict = {}

while(True):
    ask = input('Do you want to add Student? \n')
    if ask == "Y":
        sid = int(input("Enter SID - "))
        Name = str(input('Enter Name - '))
        dict[sid] = Name
        rev_dict[Name] = sid 

    elif ask == 'N':
        break

print(dict)                            #a

sorted_vals = sorted(rev_dict.keys())       #b
dict1 = {sorted_vals[i] : rev_dict.get(sorted_vals[i]) for i in range(len(dict))}
print(dict1)


sorted_keys = sorted(dict.keys())               #c
dict2 = {sorted_keys[i] : dict.get(sorted_keys[i]) for i in range(len(dict))}     
print(dict2)


ask_sid = int(input('enter sid to search - '))               #d

if ask_sid in dict.keys():
    print(f' Name of {ask_sid} is {dict[ask_sid]}')


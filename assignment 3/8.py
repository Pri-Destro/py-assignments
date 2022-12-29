set1= {1, 2, 3, 4, 5}
set2= {2, 4, 6, 8}
set3= {1, 5, 9, 13, 17}

set4 = set1 ^ set2              #a
print(f'set of elements that are in Set1 and Set2 but not both \n {set4} ')

set5 = set1 ^ set2 ^ set3        #b
print(f'set of elements that are in only one of the three sets Set1, Set2 and Set3.\n {set5} ')


set6 = set()                        #c
set6.update(set1 & set2)
set6.update(set2 & set3)
set6.update(set1 & set3)
print(f'set of elements that are exactly two of the sets Set1, Set2 and Set3. \n {set6}')


set7 = set()                    #d
for i in range(1,11):
    if i not in set1:
        set7.add(i)
print(f'set of all integers in the range 1 to 10 that are not in Set1 \n {set7}')


set8 = set()                    #e
for i in range(1,11):                           
    if i not in (set1 | set2 | set3):
        set8.add(i)
print(f'set of all integers in the range 1 to 10 that are not in Set1, Set2 and Set3 \n {set8}')


dict = {4 : ['D','Poor'] ,
        5 : ['C','Below Average'],
        6 : ['C+','Average'],
        7 : ['B','Good'],
        8 : ['B+','Very Good'],
        9 : ['A','Excellent'],
        10 : ['A+','Outstanding'] }

grade = int(input('Enter Grade - '))

if 4 <= grade <= 10:
    print(f"Your Grade is '{dict[grade][0]}' and {dict[grade][1]} Performance.")
else:
        print('Error\n Out of range')
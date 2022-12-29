day = int(input('Enter date - '))
month = int(input('Enter month - '))
year = int(input('Enter year - '))

if (1 <= day <31) & (1 <= month < 12) & (1 <= year < 2025) :
    day+=1

elif (month == 12) & (day == 31):
    year += 1
    month,day = 1,1

elif day == 31:
    month += 1
    day = 1

print(f'Next day is {day}/{month}/{year}')

income = int(input('Enter your income - '))
dependents = int(input('enter no. of dependents - '))

rate = 20

taxable_income = income - 10000 - (3000 * dependents)

tax = taxable_income * (rate/100)
print(f'your income tax is {tax}')


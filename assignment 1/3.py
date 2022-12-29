scnds = int(input('Enter seconds - '))
minutes = (scnds//60)
scnds_left = scnds % 60
print(f'{minutes} minutes and {scnds_left} seconds')
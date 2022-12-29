string = 'ABCDEFGHIJK'
i = 0
while len(string)-i*2 >= 1:
    print(' '*i, string[0 : len(string) - i*2])
    i += 1
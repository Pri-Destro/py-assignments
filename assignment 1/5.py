import math
for i in range(0,346,15):
    rad = math.radians(i)
    sine = round(math.sin(rad),4)
    cosine = round(math.cos(rad),4)

    
    print(f'{i} -- {sine} , {cosine} \n')


a:int = int(input('a oldal (cm): '))
b:int = int(input('b oldal (cm): '))

if a > 0 and b > 0:
    print(f'kerület: {2*(a+b)} cm')
    print(f'terület: {a*b} cm^2')
else: print('egyik bemenet negatív')
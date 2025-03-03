#co = float(input('Comprimento do cateto oposto: '))
#ca = float(input('Comprimento do cateto adjascente: '))
#hip = (co**2 + ca**2) ** (1/2)
#print('A hipotenusa vale: {:.2f}'.format(hip))

from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjascente: '))
hip = hypot(co, ca)
print('A hipotenusa vale: {:.2f}'.format(hip))
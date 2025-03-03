from math import sqrt

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjascente: '))
hipotenusa = sqrt(co**2 + ca**2) #a² = ca² + co²
print("A hipotenusa é: {:.2f}".format(hipotenusa))
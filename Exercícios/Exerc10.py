real = float(input("Quanto você possui em sua carteira? R$"))
dolar = real / 4.82 #Cotação 17/06/2023
euro = real / 5.29 #Cotação 17/06/2023
iene = real / 0.034 #Cotação 17/06/2023
print("Com R${:.2f} você consegue comprar US${:.2f}.".format(real, dolar))
print("Com R${:.2f} você consegue comprar €{:.2f}.".format(real, euro))
print("Com R${:.2f} você consegue comprar ¥{:.2f}.".format(real, iene))
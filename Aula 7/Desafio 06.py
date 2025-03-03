real = float(input("Quanto de dinheiro você possui na carteira? R$"))
dolar = real / 4.82 #Cotação do dia 17/06/2023
euro = real / 5.29 #Cotação do dia 17/06/2023
iene = real / 0.034 #Cotação do dia 17/06/2023
print("Com R${:.2f} você pode comprar US${:.2f}".format(real, dolar))
print("Com R${:.2f} você pode comprar €{:.2f}".format(real, euro))
print("Com R${:.2f} você pode comprar ¥{:.2f}".format(real, iene))
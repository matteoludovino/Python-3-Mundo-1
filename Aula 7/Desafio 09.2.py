preço = float(input("Qual o valor do produto? R$"))
pix = preço - (preço * 10 / 100)
parcelado = preço + (preço * 8 / 100)
print("O produto custa R${:.2f} à vista no PIX com 10% de desconto.".format(pix))
print("Parcelado, o produto recebe 8% de aumento no preço, custando agora R${:.2f}.".format(parcelado))
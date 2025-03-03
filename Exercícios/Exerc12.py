preço = int(input("Qual o valor do produto? R$"))
desconto = preço - (preço * 5 / 100)
print("O produto custava {:.2f}, mas agora com a nova promoção de 5% de desconto está custando {:.2f}!".format(preço, desconto))
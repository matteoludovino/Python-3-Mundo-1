preço = float(input("Qual o preço do produto? R$"))
#desconto = preço * 5 /100
novopreço = preço - (preço * 5 / 100)
print("O preço do produto era R${:.2f}, mas com o novo desconto de 5% da promoção agora custa R${:.2f}".format(preço, novopreço))
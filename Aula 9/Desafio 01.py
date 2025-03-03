nome = input(str('Digite um nome: '))

maiusculo = nome.upper()
minusculo = nome.lower()
qtd = len(nome.replace(' ', ''))
divide = nome.split()
contagem = divide[0]
qtdprimeiro = len(contagem)

print('Nome completo: {}'.format(str(nome)))
print('Nome em maiúsculo: {}'.format(str(maiusculo)))
print('Nome em minúsculo: {}'.format(str(minusculo)))
print('Quantidade de letras totais do nome: {}'.format(qtd))
print('Quantidade de letras do primero nome {}'.format(qtdprimeiro))
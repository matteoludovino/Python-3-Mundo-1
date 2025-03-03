nome = str(input('Digite um nome: '))

palavras = nome.split()
primeiro = palavras[0]
ultimo = palavras[-1]

print('Primeiro nome: {}'.format(primeiro))
print('Último nome: {}'.format(ultimo))
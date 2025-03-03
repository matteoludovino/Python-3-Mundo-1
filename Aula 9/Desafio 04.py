nome = str(input('Digite um nome: '))
tems = nome.count('Silva')

print(["Você não tem Silva no nome.", "Você tem Silva no nome."][bool(tems)])
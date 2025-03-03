frase = str(input('Digite uma frase: '))
procurada = 'a'

letras = frase.count('a')
primeira = frase.find(procurada)
ultima = frase.rfind(procurada)

print('Na frase aparecem {} letras "a"'.format(letras))
print('Ela aparece na posição {} pela primeira vez'.format(primeira))
print('Ela aparece na posição {} pela última vez'.format(ultima))
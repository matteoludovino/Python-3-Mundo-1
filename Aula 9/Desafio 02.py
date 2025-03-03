numero = input('Digite um número de 0 a 9999: ')

strg = numero.zfill(4)

unidade = strg[3]
dezena = strg[2]
centena = strg[1]
milhar = strg[0]

print('Milhar: {}'.format(milhar))
print('Centenas: {}'.format(centena))
print('Dezenas: {}'.format(dezena))
print('Unidades: {}'.format(unidade))
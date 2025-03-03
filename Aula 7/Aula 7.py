n1 = int(input("Digite um valor: "))
n2 = int(input("Digite outro valor: "))
print("\nOs valores digitados foram:", n1,"e",n2,"\n")
s = n1 + n2
sb = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print("A soma é igual a {}\nA subtração é igual a {}\nA multiplicação é igual a {}\nA divisão é igual a {:.4f}\nA divisão inteira é igual a {}\nA potência é igual a {}".format(s, sb, m, d, di, e))
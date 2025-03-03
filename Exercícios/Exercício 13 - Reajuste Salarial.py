salario = float(input("O salário do funcionário é de: R$"))
aumento = salario + (salario * 15 / 100)
print("O funcionário recebia R${:.2f} em seu salário, mas ele recebeu um aumento de 15%, portanto agora seu salário será R${:.2f}!".format(salario, aumento))
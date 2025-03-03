salario = float(input("Qual o salário do funcionário? R$"))
#aumento = (15 * salario)/100
novosalario = salario + (salario * 15 / 100)
print("O salário do funcionário era R${:.2f}, mas agora com o novo aumento de 15%, o salário é R${:.2f}".format(salario, novosalario))
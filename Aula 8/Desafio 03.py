from math import cos, sin, tan, radians

angulo = float(input('Digite um ângulo: '))
cosseno = cos(radians(angulo))
seno = sin(radians(angulo))
tangente = tan(radians(angulo))
print('O seno de {}° é: {:.2f}'.format(angulo, seno))
print('O cosseno de {}° é: {:.2f}'.format(angulo, cosseno))
print('O tangente de {}° é: {:.2f}'.format(angulo, tangente))
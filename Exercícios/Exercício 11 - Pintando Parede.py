largura = float(input("Qual a largura da parede? "))
altura = float(input("Qual a altura da parede? "))
area = largura * altura #Calcula a área
tinta = area / 2 #Cada litros de tinta consegue pintar 2m² de parede
print("As dimensões da parede são: {}x{}, portanto a área da parede é de {}m².".format(largura, altura, area))
print("Para pintar essa parede você precisará de {}l de tinta.".format(tinta))
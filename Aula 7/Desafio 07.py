largura = float(input("Largura da parede: "))
altura = float(input("Altura da parede: "))
area = largura * altura
tinta = area / 2 #A tinta pode pintar até 2m² da parede
print("A área da parede é de {}m², com a dimensão de {}x{}.".format(area, largura, altura))
print("Para pintar essa parede você precisará de {}l de tinta".format(tinta))
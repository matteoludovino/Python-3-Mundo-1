tc = float(input("Qual a temperatura em °C agora? "))
tf = (tc * 9 / 5) + 32
tk = tc + 273
print("A temperatura de {}°C corresponde a {}°F".format(tc, tf))
print("A temperatura de {}°C correpende a {}K".format(tc, tk))
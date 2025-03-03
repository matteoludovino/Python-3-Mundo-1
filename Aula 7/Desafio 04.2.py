m = float(input("Digite uma distância em metros: "))
km = m / 1000 #Quilômetros
hm = m / 100 #Hectômetros
dam = m / 10 #Decâmetros
dm = m * 10 #Decímetros
cm = m * 100 #Centímetros
mm = m * 1000 #Milímetros
print("{}m em quilômetros = {}km\n{}m em hectômetros = {}hm\n{}m em decâmetros = {}dm".format(m, km, m, hm, m, dam))
print("{}m em decímetros = {:.0f}dm\n{}m em centímetros = {:.0f}cm\n{}m em milímetros = {:.0f}mm".format(m, dm, m, cm, m, mm))
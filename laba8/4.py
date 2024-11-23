chisla = input("Введи числа: ")
res = chisla.split()
for a in range(len(res)):
    res[a] = int(res[a])
srznach = sum(res) / len(res)
print("Среднее значиение", srznach)
nize = []
for i in res:
    if i < srznach:
        nize.append(str(i))
print("Числа меньше среднего значения: "," ".join(nize))
bolshe = []
for g in res:
    if g > srznach:
        bolshe.append(str(g))
print("Числа больше среднего значения: "," ".join(bolshe))
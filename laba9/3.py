n = int(input("Введите количество координат: "))
m = 2  # n - строка, m - столбец
matrix = []
for i in range(n):  # 2 строки, вводим коорды сокровищ
    line = []
    for j in range(m):
        line.append(int(input("Введи координаты одного из сокровищ: ")))
    matrix.append(line)
print("Координаты сокровищ:", matrix)

Alex = []
for i in range(m):
    koord = int(input("Введи координаты Александра: "))
    Alex.append(koord)
print("Координаты Александра:", Alex)

# расстояние между точками
resi = []
for i in range(n):
    res = ((matrix[i][0] - Alex[0]) ** 2 + (matrix[i][1] - Alex[1]) ** 2) ** 0.5
    res = round(res, 1) # округляем до десятых
    resi.append((f"{res} метров, {matrix[i]}"))

resi.sort()
print("Сокровища в порядке отдаления: ", resi)
print("Ближайшее сокровище: ", resi[0]) 


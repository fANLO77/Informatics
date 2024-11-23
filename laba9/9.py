import random
n=4
matrix=[]
for i in range(n): # заполняем звездами
    line = []
    for j in range(n):
        a='*'
        line.append(a)
    matrix.append(line)


plot = [] # ставим плоты
while len(plot) < 4:
    oneship = [random.randint(0, n - 1), random.randint(0, n - 1)]
    if oneship not in plot: # проверяем не занято ли место другим плотом
        plot.append(oneship)

bomb = [random.randint(0, n - 1), random.randint(0, n - 1)]
while bomb in plot: # пока бомба в корабле - меняем позицию
    bomb = [random.randint(0, n - 1), random.randint(0, n - 1)]

popitka = 0 # счетчик попыток
kills = 0 #с четчик киллов

while kills < 4:

    for i in range(n): # выводим матрицу пока не убьем 4 раза
        for j in range(n):
            print(matrix[i][j], end=' ')
        print()

    x, y = map(int, input("Куда стрельнуть? (например, 1 2): ").split())

    if [x, y] in bomb:
        print("BOMB")
        break

    if [x, y] in plot:
        print("Потопили")
        matrix[x][y]='X'
        plot.remove([x, y])
        kills += 1
    else:
        print("Промах\n")

    popitka += 1

if kills == 4:
    print(f"Молодец, попал с {popitka} попытки.")
else:
    print("Не сегодня")
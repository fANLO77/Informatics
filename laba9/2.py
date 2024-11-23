def magic_square(n):
    magic = []  # создаем пустую матрицу
    for i in range(n):
        row = [0] * n
        magic.append(row)  # добавляем пустую строку в матрицу

    i = 0  # начальная строка
    j = n // 2  # начальный столбец

    for num in range(1, n**2 + 1):
        magic[i][j] = num  # Заполняем текущую ячейку

        i_new = (i - 1) % n  # новая строка
        j_new = (j + 1) % n  # новый столбец

        if magic[i_new][j_new] != 0:  # если ячейка занята то переходим вниз
            i += 1  
        else:
            i = i_new
            j = j_new

    return magic

# выводим это месево
n = 3
square = magic_square(n)

for row in square:
    print(row)

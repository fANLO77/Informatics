n = int(input("Введите размер матрицы: "))

matrix = []
print("Введите элементы матрицы строками:")
for i in range(n):
    stroka = input().split() 
    stroka = list(map(int, stroka))  
    matrix.append(stroka)
print(matrix)

for j in range(n):  # т.к. главная диагональ имеет [x][x] координаты(одинаковые)
    vrem_matrix = matrix[j][j]  # закидываем элемент во временный список
    matrix[j][j] = matrix[n - j - 1][
        j]  # [n-j-1] из 3-й строки вычитаем 0-ую(т.е. переставляем [0][2] в [0][0]; (-1) тк это [2][2] а не 3 3
    matrix[n - j - 1][j] = vrem_matrix  # переставляем матрицу которую забирали с [0][0] на место, откуда взяли [0][2]

print("Результат транспонирования")
for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=' ')
    print()


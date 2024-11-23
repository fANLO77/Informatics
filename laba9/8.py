n = int(input("Введите количество строк матрицы(N): "))
m = int(input("Введите количество строк матрицы(M): "))

matrix = []
for i in range(n): # заполняем ноликами
    line = []
    for j in range(m):
        a=0
        line.append(a)
    matrix.append(line)


for i in range(n): # заполняем единичками [1][1]
    for j in range(m):
        matrix[0][j] = 1
        matrix[i][0] = 1


for i in range(1,n): # заполняем остатки
    for j in range(1,m):
        matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]

for i in range(n): 
    for j in range(m):
        print(matrix[i][j], end=' ')
    print()

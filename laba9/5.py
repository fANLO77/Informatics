n = int(input("Введите N: "))
m = int(input("Введите M: "))
matrix = []
for i in range(n):
    line = []
    for j in range(m):
        line.append(int(input("Введи элемент: ")))
    matrix.append(line)

print("Матрица")
for i in range(n):
    for j in range(m):
        print(matrix[i][j], end=' ')
    print()

T = []
for j in range(m):
    transline = []
    for i in range(n):
        transline.append(matrix[i][j])
    T.append(transline)

print("Транспонированная матрица")
for i in range(m):
   for j in range(n):
       print(T[i][j], end=' ')
   print()


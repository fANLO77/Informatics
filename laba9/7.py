n = int(input("Введите количество строк матрицы(N): "))
m = int(input("Введите количество строк матрицы(M): "))

matrix = []                       
print("Введите элементы матрицы(1 или 0):")
for i in range(n):
    line = []
    for j in range(m):
        a = int(input())
        if a == 1 or a == 0:
            line.append(a)
        else:
            print("Не балуйся")
    matrix.append(line)

for i in range(n):         
    for j in range(m):
        print(matrix[i][j], end=' ')
    print()

cheloveki = int(input("Введите количество человек: "))
proverka = False 
for i in range(n):
    svobodno = 0 #счетчик мест, если набирается 'cheloveki' мест - выводится этот ряд
    for j in range(m):
        if matrix[i][j] == 0:
            svobodno += 1
            if svobodno == cheloveki: #если свободные места=людям - то збс
                proverka = True
                print(f"Можно купить места в {i+1} ряду")
                break
        else:
            proverka = False
            svobodno = 0
if not proverka:
    print("Соболезную")
else:
    print()


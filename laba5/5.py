print("Введите стороны треугольника")
a = int(input("Первая сторона: "))
b = int(input("Вторая сторона сторона: "))
c = int(input("Третья сторона: "))
if a == b == c:
    print("Ваш треугольник равносторонний")
elif a == b or a == c or b == c:
    print("Ваш треугольник равнобедренный")
else:
    print("Ваш треугольник разносторонний")
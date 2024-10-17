s = input("Введи ноиер билета:")
if len(s) == 6:
    if int(s[0]) + int(s[1]) + int(s[2]) == int(s[3]) + int(s[4]) + int(s[5]):
        print("Поздравляю! Ваш билет - счастливый")
    else:
        print("Обычный билет")
else:
    print("Некорректный билет")

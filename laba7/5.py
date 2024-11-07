def haiku(text):
    c=0
    lines = text.split('//')
    kolvoslov = ["а","е","ё","и","о","у","ы","э","ю","я"]
    if kolvoslov in text:
        c+=1
    if len(lines) == 3:
         return "Хайку!"
    else:
        return "Не хауку.Должно быть 3 строки"
vvedihaiku = input("Введи хауку: ")
print(haiku(vvedihaiku))
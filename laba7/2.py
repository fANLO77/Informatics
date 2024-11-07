def perevorot(text):
    slova = text.split()
    if len(slova) == 2:
        return f"{slova[1]} {slova[0]}"
    else:
        return "Ошибка! Некорректное количество слов"
vvedislova = input("Введи словосочетание: ")
print(perevorot(vvedislova))
    
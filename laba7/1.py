def F(text):
    slova = text.split()
    res = []
    for i in range(len(slova)):
        if slova[i]!=slova[i - 1]:
            res.append(slova[i])
    return " ".join(res)
vveditext = input("Введи текст с ошибками: ")
print(F(vveditext))
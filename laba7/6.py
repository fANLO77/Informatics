def rasshifrovka(shifr):
    if "#" not in shifr:
        return "Ошибка! Отсутствует символ #"
    shifr = shifr[:-1]
    shifr_list = [""] * len(shifr)
    left = 0
    right = len(shifr) - 1
    for i in range(len(shifr)):
        if i%2==0:
            shifr_list[left] = shifr[i]
            left+=1
        else:
            shifr_list[right] = shifr[i]
            right-=1
    return "".join(shifr_list)

zashifr = input("Введи зашифрованный текст:")
print(rasshifrovka(zashifr))
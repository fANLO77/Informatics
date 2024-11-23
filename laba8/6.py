import random

count = 0
posled = []
while True:
    vbros = random.randint(0, 1)
    if vbros == 0:
        podbros = 'O'
        posled.append('O')
    else:
        podbros = 'P'
        posled.append('P')
    count+=1
    if len(posled) >= 3 and posled[-3:] == ['O', 'O', 'O'] or posled[-3:] == ['P', 'P', 'P']:
        break
print("Последовательность: ", " ".join(posled), end="  ")
print("Попытка: ", count)
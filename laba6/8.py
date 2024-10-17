a = str(input("Введи двоичный код числа: "))
des = 0
step = 0
for i in range(len(a)-1,-1,-1):
    if a[i] == '1':
        des += 2**step
    step+=1
if not '1' in a or not '0' in a:
    print("Некоректно заданное число в двоичной системе")
else:
    print("Твоё число в десятичной системе счисления равно:", des)
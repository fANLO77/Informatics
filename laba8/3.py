a = input("Введи числа: ")
res = a.split()
otvet = []
for i in range(0,len(res)-1):
    if res[i] < res[i+1]:
        otvet.append(res[i+1])
    else:
        continue
if len(otvet)!=0 and len(otvet)>1:
    b = " ".join(otvet)
    print(b)
else:
    print("Мало чисел либо они не подходят под условие")
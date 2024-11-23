a = input("Введи рост учеников: ")
rost = a.split()
for i in range(len(rost)):
    rost[i] = int(rost[i])
    if rost[i] > 230 or rost[i] <= 0:
        print("Не балуйся с числами, небывает таких людей")
a_rost = int(input("Введи рост Андрея: "))
if a_rost > 230 or a_rost <= 0:
    print("Тебе же сказали не баловаться с числами")
else:
    count = 0
    for g in rost:
        if g >= a_rost:
            count+=1
    nomer_a = count + 1
    print("Номер Андрея в строю: ",nomer_a)
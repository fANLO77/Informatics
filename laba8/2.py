import random
a = input("Введи свой билет: ")
svoibilet = a.split()
bilet = sorted(random.sample(range(1,50),6))
print(f"{bilet} числа для выйгрыша" )
if len(svoibilet)!= 6:
    print("Вы ввели некоректный билет")
else:
    if svoibilet == bilet:
        print(f"Ты выйграл главный приз! Ваш билет{svoibilet} совпал с чисами для выйгрыша{bilet}")
    else:
        print(f"Ты не выйграл главный приз(... Ваш билет{svoibilet} не совпал с чисами для выйгрыша{bilet}. Попробуй в другой раз")
    
a = input("Введите название месяца: ")
if a == "Февраль":
    print("Этот месяц может состоять как из 28, так и из 29 дней, учитывая фактор високосного года")
elif a in ("Январь", "Март", "Май", "Июль", "Август", "Октябрь", "Декабрь"):
    print("В этом месяце 31 день")
elif a in ("Апрель", "Июнь", "Сентябрь", "Ноябрь"):
    print("В этом месяце 30 дней")
else:
    print("Такого месяца не существует")
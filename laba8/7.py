def card(nomer_card):
    tsifri = []
    for d in str(nomer_card):
        tsifri.append(int(d))

    for i in range(len(tsifri) - 2, -1, -2):
        doubled = tsifri[i] * 2

        if doubled < 10:
            tsifri[i] = doubled
        else:
            tsifri[i] = doubled - 9

    return sum(tsifri) % 10 == 0

nomer_card = input("Введи номер карты для проверки: ").strip()

if card(nomer_card):
    print(f"{nomer_card}: Корректный номер")
else:
    print(f"{nomer_card}: Некорректный номер")

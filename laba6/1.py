rost = []

while rost!=0:
    ros = int(input("Введи рост: "))
    if ros == 0:
        break
    if ros > 0:
        rost.append(ros)
if len(rost) < 2:
    print("Некого сравнивать")
else:
    maxs = max(rost)
    mins = min(rost)
print("Рост самого высокого:", maxs)
print("Рост самого низкого:", mins)


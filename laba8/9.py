n = int(input("Всего комнат: "))
count = 0
for i in range(n):
    p = input("Введи кол-во человек которые уже живут в комнате: ",)
    q = input("введи кол-во человек которые могут жить в этой комнате: ")
    p = int(p)
    q = int(q)
    if q - p >= 2:
        count +=1 
if n <= 0  or p < 0 or q <= 0:
    print("Не балуйся с числами")
else:
    print("Кол-во комнат в которых могут жить ребята: ", count)


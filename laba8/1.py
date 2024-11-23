a = input('Введи символы через пробел: ').split(' ')

for_num = []
for_buk = []

num = '1234567890'
buk = 'qwertyuiopasdfghjklzxcvbnm'

for i in a:
    if i in num:
        for_num.append(i)
    elif i in buk:
        for_buk.append(i)

del a

print(for_buk)
print(for_num)

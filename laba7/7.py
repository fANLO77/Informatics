import random
import string

def paroli(dlina,zaglav,stroch,tsifri,specsimvol):
    parol = ""
    while zaglav != "no" or stroch  != "no" or tsifri != "no" or specsimvol != 'no':
        if zaglav == "yes":
            parol += string.ascii_uppercase
        if stroch == "yes":
            parol += string.ascii_lowercase
        if tsifri == "yes":
            parol += string.digits
        if specsimvol == "yes":
            parol += string.punctuation  
        password = "".join(random.choice(parol) for i in range(dlina))
        return password
    else:
        print("Выбери какие нибудь символы для пароля")

dlina = int(input("Введи длину пароля: "))
zaglav = input("Нужны ли заглавные буквы: ")
stroch = input("Нужны ли строчные буквы: ")
tsifri = input("Нужны ли цифры: ")
specsimvol = input("Нужны ли специальные символы: ")

generate_password = paroli(dlina,zaglav,stroch,tsifri,specsimvol)

print(generate_password)
import random

def game():
    secret = random.randint(1, 10)
    k = 0
    print("Хорошо, я загадал число. Попробуй его отгадать")
    while 1:
        num = int(input("> "))
        if num == secret:
            print("Поздравляю! Вы угадали!")
            a = input("Хотншь сыграть снова? ")
            if a == "yes":
                return game()
            elif a == "no":
                break
        else:
            k+=1
            print(f"Нее, ты не угадал. Попробуй снова. Попытка № {k}")
            if num > secret:
                print("Твоё число болше загаданного")
            else:
                print("Твоё число меньше загаданного")

game()

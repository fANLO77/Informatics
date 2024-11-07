def zamena(text):
    while "не плоха" in text or "не плохой" in text:
        text = text.replace("не плоха","хороша")
        text = text.replace("не плохой","хороший")
        return text
vveditext = input("Введи текст: ")
print(zamena(vveditext))
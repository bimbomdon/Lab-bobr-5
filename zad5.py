def vvod():
    return input("Введите текст: ")

def obrabotka(text):
    # Обработка пустой строки
    if not text.strip():
        return ""

    # Разбиваем текст на слова (по пробелам)
    slova = text.split()

    # Переворачиваем каждое слово с помощью срезов [::-1]
    perevernutye_slova = [slovo[::-1] for slovo in slova]

    # Собираем текст обратно через пробел
    return " ".join(perevernutye_slova)

def vyvod(rezultat):
    if not rezultat:
        print("Строка пустая.")
    else:
        print("Результат:", rezultat)

# Запуск
tekst = vvod()
res = obrabotka(tekst)
vyvod(res)
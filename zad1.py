def vvod():
    """Спрашивает текст у пользователя."""
    # Просто читаем строку. Если пустая — вернётся пустая строка, 
    # это потом проверит функция обработки.
    return input("Введите текст: ")

def obrabotka(text):
    """Считает слова, находит самое длинное и самое короткое."""
    # Обработка пустой строки
    if not text.strip():
        return 0, "Нет", "Нет"

    # Разбиваем текст по пробелам, отбрасывая пустые куски
    slova = text.split()
    kolichestvo = len(slova)

    # Ищем самое длинное и короткое
    samoe_dlinnoe = slova[0]
    samoe_korotkoe = slova[0]

    for slovo in slova:
        if len(slovo) > len(samoe_dlinnoe):
            samoe_dlinnoe = slovo
        if len(slovo) < len(samoe_korotkoe):
            samoe_korotkoe = slovo

    return kolichestvo, samoe_dlinnoe, samoe_korotkoe

def vyvod(kolichestvo, dlinnoe, korotkoe):
    """Выводит результаты."""
    if kolichestvo == 0:
        print("Строка пустая или содержит только пробелы.")
    else:
        print(f"Количество слов: {kolichestvo}")
        print(f"Самое длинное слово: '{dlinnoe}' (длина {len(dlinnoe)})")
        print(f"Самое короткое слово: '{korotkoe}' (длина {len(korotkoe)})")

# Запуск
tekst = vvod()
kol, dlin, kor = obrabotka(tekst)
vyvod(kol, dlin, kor)
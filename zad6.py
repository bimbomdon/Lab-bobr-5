def vvod():
    """Спрашивает текст у пользователя."""
    return input("Введите текст: ")

def obrabotka(text):
    """Удаляет повторяющиеся символы, сохраняя порядок."""
    # Обработка пустой строки
    if not text:
        return ""

    unikalnye = ""
    # Множество (set) запоминает символы, которые мы уже видели
    videli = set()

    for simvol in text:
        # Если символ еще не встречался — добавляем в результат
        if simvol not in videli:
            unikalnye += simvol
            videli.add(simvol) # Запоминаем, что этот символ уже был

    return unikalnye

def vyvod(rezultat):
    """Выводит результат."""
    if not rezultat:
        print("Строка пустая или не содержит символов.")
    else:
        print("Результат:", rezultat)

# Запуск
tekst = vvod()
res = obrabotka(tekst)
vyvod(res)
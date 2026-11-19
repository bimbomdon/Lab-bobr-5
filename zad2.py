def vvod():
    """Спрашивает текст у пользователя."""
    return input("Введите текст для проверки на палиндром: ")

def obrabotka(text):
    """Проверяет строку на палиндром."""
    # 1. Обработка пустой строки
    if not text.strip():
        return None # Возвращаем None, чтобы показать, что строка пустая

    # 2. Очистка строки: оставляем только буквы и цифры, приводим к нижнему регистру
    ochishchennaya = ""
    for simvol in text:
        # isalnum() возвращает True, если символ — это буква или цифра
        if simvol.isalnum():
            ochishchennaya += simvol.lower()

    # Если после очистки ничего не осталось (были только спецсимволы)
    if not ochishchennaya:
        return None

    # 3. Проверка на палиндром
    # Сравниваем очищенную строку с её перевёрнутой копией
    if ochishchennaya == ochishchennaya[::-1]:
        return True
    else:
        return False

def vyvod(rezultat):
    """Выводит результат проверки."""
    if rezultat is None:
        print("Ошибка: строка пустая или не содержит букв и цифр.")
    elif rezultat:
        print("Это палиндром!")
    else:
        print("Это НЕ палиндром.")

# Запуск
tekst = vvod()
res = obrabotka(tekst)
vyvod(res)
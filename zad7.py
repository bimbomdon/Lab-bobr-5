def vvod():
    """Спрашивает текст у пользователя."""
    return input("Введите текст: ")

def obrabotka(text):
    """Преобразует строку в camelCase."""
    # Обработка пустой строки
    if not text.strip():
        return ""

    # Разбиваем строку на слова (убираем лишние пробелы)
    slova = text.split()

    # Берем первое слово и приводим его полностью к нижнему регистру
    # (например, "ПРИВЕТ" станет "привет")
    rezultat = slova[0].lower()

    # Проходим по всем словам, начиная со второго
    for slovo in slova[1:]:
        # Берем первую букву слова, делаем её заглавной, 
        # а остальные буквы — строчными, и приклеиваем к результату
        rezultat += slovo[0].upper() + slovo[1:].lower()

    return rezultat

def vyvod(rezultat):
    """Выводит результат."""
    if not rezultat:
        print("Строка пустая.")
    else:
        print("Результат:", rezultat)

# Запуск
tekst = vvod()
res = obrabotka(tekst)
vyvod(res)
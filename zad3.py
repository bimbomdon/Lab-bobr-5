def vvod():
    """Спрашивает текст и подстроки для замены."""
    text = input("Введите исходный текст: ")
    a = input("Что ищем (подстрока a): ")
    b = input("На что меняем (подстрока b): ")
    return text, a, b

def obrabotka(text, a, b):
    """Заменяет подстроку a на b и считает количество замен."""
    # Обработка пустой строки
    if not text:
        return text, 0
    
    # Обработка пустой подстроки для поиска (иначе будет ошибка или бесконечная замена)
    if not a:
        return text, 0

    # Считаем, сколько раз подстрока 'a' встречается в тексте
    kolichestvo = text.count(a)

    # Если ничего не нашли, можно даже не делать замену
    if kolichestvo == 0:
        return text, 0

    # Выполняем замену
    novyy_text = text.replace(a, b)

    return novyy_text, kolichestvo

def vyvod(novyy_text, kolichestvo):
    """Выводит результат замены."""
    if kolichestvo == 0:
        print("Подстрока не найдена. Текст остался без изменений.")
    else:
        print(f"Количество замен: {kolichestvo}")
        print(f"Новый текст: {novyy_text}")

# Запуск
tekst, poisk, zamena = vvod()
novyy, kol = obrabotka(tekst, poisk, zamena)
vyvod(novyy, kol)
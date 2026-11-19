def vvod():
    """Спрашивает текст, режим работы и сдвиг."""
    print("1 - Зашифровать")
    print("2 - Расшифровать")
    rezhim = input("Выбор: ")
    
    text = input("Введите текст: ")
    
    try:
        k = int(input("Введите сдвиг (k): "))
    except ValueError:
        print("Ошибка: сдвиг должен быть целым числом.")
        return "0", "", 0

    return rezhim, text, k

def obrabotka(text, k, deystvie):
    """Шифрует или расшифровывает текст."""
    # Обработка пустой строки
    if not text:
        return ""

    # Если расшифровываем, то просто делаем сдвиг в обратную сторону
    if deystvie == "2":
        k = -k

    rezultat = ""
    
    for simvol in text:
        # Проверяем, является ли символ русской или английской буквой
        if simvol.isalpha():
            
            # --- Обработка английских букв ---
            if 'a' <= simvol <= 'z':
                base = ord('a')
                # ord() переводит букву в код, chr() — обратно в букву.
                # % 26 нужно, чтобы после 'z' идти на 'a'.
                novyy_code = (ord(simvol) - base + k) % 26 + base
                rezultat += chr(novyy_code)
                
            elif 'A' <= simvol <= 'Z':
                base = ord('A')
                novyy_code = (ord(simvol) - base + k) % 26 + base
                rezultat += chr(novyy_code)

            # --- Обработка русских букв ---
            elif 'а' <= simvol <= 'я':
                base = ord('а')
                novyy_code = (ord(simvol) - base + k) % 32 + base
                rezultat += chr(novyy_code)
                
            elif 'А' <= simvol <= 'Я':
                base = ord('А')
                novyy_code = (ord(simvol) - base + k) % 32 + base
                rezultat += chr(novyy_code)
            
            # Если буква 'ё' (она выбивается из порядка кодов)
            elif simvol == 'ё' or simvol == 'Ё':
                # Оставляем без изменений или обрабатываем отдельно
                rezultat += simvol
                
        else:
            # Пробелы, цифры и знаки препинания не шифруем
            rezultat += simvol

    return rezultat

def vyvod(rezultat):
    """Выводит результат."""
    if not rezultat:
        print("Строка пустая.")
    else:
        print("Результат:", rezultat)

# Запуск
rezhim, tekst, sdvig = vvod()
if rezhim != "0":
    res = obrabotka(tekst, sdvig, rezhim)
    vyvod(res)
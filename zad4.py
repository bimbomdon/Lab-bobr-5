def vvod():
    """Спрашивает текст у пользователя."""
    return input("Введите текст: ")

def obrabotka(text):
    """Считает гласные, согласные и цифры."""
    # Обработка пустой строки
    if not text:
        return 0, 0, 0

    # Задаем наборы букв
    glasnye = "аеёиоуыэюяaeiouy" # русские и английские гласные
    soglasnye = "бвгджзйклмнпрстфхцчшщbcdfghjklmnpqrstvwxyz" # русские и англ. согласные

    kol_glasnyh = 0
    kol_soglasnyh = 0
    kol_cifr = 0

    for simvol in text:
        # Приводим символ к нижнему регистру, чтобы 'А' и 'а' считались одинаково
        s = simvol.lower()

        if s in glasnye:
            kol_glasnyh += 1
        elif s in soglasnye:
            kol_soglasnyh += 1
        elif s.isdigit(): # Проверяем, является ли символ цифрой
            kol_cifr += 1

    return kol_glasnyh, kol_soglasnyh, kol_cifr

def vyvod(glas, soglas, cifry):
    """Выводит результаты подсчета."""
    print("\n--- Результаты ---")
    print(f"Гласных букв: {glas}")
    print(f"Согласных букв: {soglas}")
    print(f"Цифр: {cifry}")

# Запуск
tekst = vvod()
g, s, c = obrabotka(tekst)
vyvod(g, s, c)
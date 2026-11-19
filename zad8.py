import re

def vvod():
    """Спрашивает текст у пользователя."""
    return input("Введите текст с числами: ")

def obrabotka(text):
    """Извлекает все числа из текста и считает их сумму."""
    # Обработка пустой строки
    if not text:
        return [], 0

    # Регулярное выражение для поиска чисел (целых и дробных, с минусом или без)
    # -?            : необязательный минус
    # \d+           : одна или более цифр
    # (\.\d+)?      : необязательная точка и цифры после неё (для дробей)
    pattern = r"-?\d+(?:\.\d+)?"
    
    # findall находит все совпадения и возвращает список строк
    nashli_stroki = re.findall(pattern, text)

    # Превращаем найденные строки в числа (float) и складываем в список
    chisla = []
    for s in nashli_stroki:
        chisla.append(float(s))

    # Считаем сумму
    summa = sum(chisla)

    return chisla, summa

def vyvod(chisla, summa):
    """Выводит найденные числа и их сумму."""
    if not chisla:
        print("В тексте не найдено ни одного числа.")
    else:
        print(f"Найденные числа: {chisla}")
        print(f"Их сумма: {round(summa, 4)}")

# Запуск
tekst = vvod()
naydennye, itog = obrabotka(tekst)
vyvod(naydennye, itog)
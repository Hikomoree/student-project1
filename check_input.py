
"""
Атрибуты модуля:
    Методы:
        check_num(text) - проверяет данные на то можно ли перевести их в float.
        input_num(number) - Обеспечивает проверку ввода пользователя.
"""

def input_num(number: str) -> bool:
    """
    Обеспечивает проверку ввода пользователя.

    Параметры:
        str: str_for_input - строка для вывода пользователю, что надо вводить.

    Возврат:
        bool: result - хранит в себе истину, если правильный ввод.
    """
    if check_num(number):
        result = True
    else:
        print("Вы ввели не число, повторите ввод \n")
        result = False

    return result

def check_num(text: str) -> bool:
    """
    Проверяет данные на то можно ли перевести их в float.


    Параметры:
        str: text - данные для проверки на число.

    Возврат:
        bool: result - хранит в себе результат проверки.
    """

    result = True
    try:
        num = float(text)
    except ValueError:
        result = False

    return result

"""
Атрибуты модуля:
    Методы:
        calculate_sred(*numbers) -  Обеспечивает подсчет среднего значения чисел в списке.
"""

def calculate_sred(*numbers: tuple) -> float:
    """
    Обеспечивает подсчет среднего значения чисел в списке.

    Параметры:
        tuple of float: numbers - кортеж чисел.

    Возврат:
        float: result - хранит среднее значение.
    """
    nsum = 0
    nlen = 0
    for n in numbers:
        nsum += n
        nlen += 1
    result = nsum / nlen

    return result

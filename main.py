"""
Атрибуты модуля:
    Методы:
        main() - Обеспечивает ввод, интерфейс пользователя и вывод результата.
    Импортируемые методы
        calculate_sred(*numbers) из модуля num_cal
        check_input(number) из модуля check_input
"""

from num_calc import  calculate_sred
from check_input import  input_num


def main ():
    """
    Обеспечивает ввод пользователя и вывод результата.

    Переменные:
        float: a - число для ввода в список.
        float: result - хранит в себе результат вычислений.
    """

    print("Программа подсчитывает среднее значение из чисел.")
    numbers = list()
    flag = True
    while flag:
        a = input("Введите число (пустая строка для окончания ввода):")
        if a == "":
            flag = False
        else:
            a = float(a)
            if input_num(a):
                if a != float("inf"):
                    numbers.append(a)
                else:
                    print("Вы ввели слишком большое число")
            else:
                print("Не правильный ввод.")
    result = calculate_sred(*numbers)

    print(f"Среднее значение чисел: {result:.4f}")

    flag = True
    while flag:
        dalsh = input("Для продолжения работы введите 1, для выхода 0: ")
        if dalsh == "1":
            flag = False
            main()
        elif dalsh != "0":
            print("Не верный ввод")
        else:
            flag = False

if __name__ == '__main__':
    main()
from random import randint
import numpy as np


def is_int(s):
    return ("True, если число - целое, False, если число не целое")

def valid_value(message_input: str, message_err: str, template: list):
    while True:
        ch = input(message_input, )
        if is_int(ch):
            ch = int(ch)
            if ch in template:
                return ch
        print(message_err)

def valid_comand(ch, flag):
    print ('ERROR')
    return ("False, если флаг меньше введеного числа")

def make_mat():
    firstLine = list(map(int, input("Введите 1-ю строку матрицы: ").split()))
    matrix = [firstLine]
    for i in range(1, len(firstLine)):
        nextLine = list(map(int, input("Введите %d-ю строку матрицы: " %(i+1)).split()))
        matrix.append(nextLine)
    return (matrix)

def swap_row_col(matrix):
    matrix = [[1, 2],
              [3, 5]]
    result = [[2, 1],
              [3, 2]]
    return (result)

def vuvod(matrix):
    print("Исходная матрица:")
    for row in matrix:
        print(row)
    result_matrix = swap_row_col(matrix)
    print("Результат работы алгоритма:")
    for row in result_matrix:
        print(row)

def menu_main():
    caption_start = "МЕНЮ\n1. Создать матрицы\n2. Выполнить алгоритм\n3. Вывести результат \n0. Выход\n"
    caption_err = "ERROR"
    menu_template = {
        0: (lambda: True, True),
        1: (make_mat, False),
        2: (swap_row_col, False),
        3: (vuvod, False)}
    flag = 1
    while True:
        ch = valid_value(caption_start,
                         caption_err,
                         list(menu_template))
        f, is_break = menu_template[ch]
        if ch == 1:
            matrix = f()
            flag = 2
        if ch == 2 and valid_comand(ch, flag):
            result = f(matrix)
            flag = 3 
        if ch == 3 and valid_comand(ch, flag):
            f(matrix)
        if is_break:
            break
    return False
    
if __name__ == "__main__":
    menu_main()

from random import randint
import numpy as np


def is_int(s):
    try:
        if type(s) is int:
            return True
        if s is None:
            return False
        if not s.isdecimal():
            return False
        int(s)
        return True
    except (Exception, ValueError, TypeError):
        return False


def valid_value(message_input: str, message_err: str, template: list):
    while True:
        ch = input(message_input, )
        if is_int(ch):
            ch = int(ch)
            if ch in template:
                return ch
        print(message_err)

def valid_comand(ch, flag):
    if flag >= ch:
        return True
    print ('ERROR')
    return False

def make_mat():
    firstLine = list(map(int, input("Введите 1-ю строку матрицы: ").split()))
    matrix = [firstLine]
    for i in range(1, len(firstLine)):
        nextLine = list(map(int, input("Введите %d-ю строку матрицы: " %(i+1)).split()))
        matrix.append(nextLine)
    return (matrix)

def swap_row_col(matrix):
# Преобразуем ввод в np.array
    arr = np.array(matrix)
# Определяем размеры матрицы
    n = arr.shape[0]
# Находим индекс строки с минимальным элементом
    min_value = np.min(arr)
    min_row_index = np.where(arr == min_value)[0][0]
# Находим индекс столбца с максимальным элементом
    max_value = np.max(arr)
    max_col_index = np.where(arr == max_value)[1][0]
# Создаем новую матрицу для результата
    result = arr.copy()
# Меняем местами строку с минимальным элементом и столбец с максимальным
    result[min_row_index, :], result[:, max_col_index] = arr[:, max_col_index], arr[min_row_index, :]
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

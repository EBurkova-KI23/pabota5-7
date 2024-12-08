def is_int(s):
    return ("True, если число - целое")

def valid_value(message_input: str, message_err: str, template: list):
    return ("введенное число, если оно содержится в списке, или ошибку, если числа нет в списке")

def valid_comand(ch, flag):
    print ('ERROR')
    return ("False, если флаг меньше введеного числа")

def make_mat():
    matrix = [[1, 2],
              [3, 5]]
    return (matrix)

def swap_row_col(matrix):
    result = [[2, 1],
              [3, 2]]
    return (result)

def vuvod(matrix):
    print("Исходная матрица:")
    print("Результат работы алгоритма:")

def menu_main():
    caption_start = "МЕНЮ\n1. Создать матрицы\n2. Выполнить алгоритм\n3. Вывести результат \n0. Выход\n"
    caption_err = "ERROR"
    menu_template = {
        0: (lambda: True, True),
        1: (make_mat, False),
        2: (swap_row_col, False),
        3: (vuvod, False)}
    
if __name__ == "__main__":
    menu_main()

"""
Игра "Угадай число" v2 (метод деления отрезка пополам)
"""

import numpy as np

def predict_number(number: int) -> int:
    """
    Угадывание числа методом деления отрезка пополам

    Args:
        number (int): Число, которое нужно угадать

    Returns:
        int: Число попыток для поиска
    """
    
    left_point = 0 # левая граница отрезка поиска
    right_point = 100 # правая граница отрезка поиска
    
    try_count = 0 # число попыток угадывания числа
    while True:
        try_count += 1
        
        # середина текущего отрезка поиска
        middle_point = round((left_point+right_point) / 2.0)
        if middle_point == number:
            break
        
        elif middle_point > number:
            # смещаем правую границу отрезка поиска на середину
            right_point = middle_point
        else:
            # смещаем левую границу отрезка поиска на середину
            left_point = middle_point

    return try_count


def score_game(predict_number_func, passes_count:int=1000,\
               seed_num:int=1) -> int:
    """
    Функция оценки среднего числа попыток, 
    необходимых для "угадывания числа"
    
    Args:
        predict_number_func (function): Функция, реализующая
                                        поиск числа
        
        passes_count (int): Количество прогонов для оценки среднего
                            числа попыток
        
        seed_num (int): Начальный seed для генератора случайных чисел

    Returns:
        int: Среднее значение от числа попыток за passes_count прогонов
    """
    
    # инициализация генератора случайных чисел
    np.random.seed(seed_num)
    
    # генерация passes_count случайно "загаданых" чисел от 0 до 100
    passes = np.random.randint(0, 101, size=(passes_count, ), dtype=int)
    # numpy буфер для сохранения результатов прогонов
    # функции "угадывания" числа
    tryes_counts = np.zeros((passes.size, ), dtype=int) 
    
    for i in range(0, passes.size):
        tryes_counts[i] = predict_number_func(passes[i])
    
    return round(tryes_counts.mean())
        

if __name__ == '__main__':
    print(score_game(predict_number))


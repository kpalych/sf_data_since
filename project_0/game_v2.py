"""
Игра "Угадай число" v3 (оптимальный алгоритм: метод деления отрезка пополам)
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
    
    left_point = 0
    right_point = 100
    
    try_count = 0
    while True:
        try_count += 1
        
        cur_number = round((left_point+right_point) / 2.0)
        if cur_number == number:
            break
        
        elif cur_number > number:
            tmp_left_point = round((cur_number+left_point) / 2.0)
            if tmp_left_point > number:
                right_point = tmp_left_point
            elif tmp_left_point < number:
                left_point = tmp_left_point
            else:
                left_point = tmp_left_point
                right_point = tmp_left_point
                
        else:
            tmp_right_point = round((cur_number+right_point) / 2.0)
            if tmp_right_point < number:
                left_point = tmp_right_point
            elif tmp_right_point > number:
                right_point = tmp_right_point
            else:
                left_point = tmp_right_point
                right_point = tmp_right_point
      
        if left_point == right_point:
            break
        
    return try_count


def score_game(predict_number_func, seed_num=1) -> int:
    """
    Game algorythm estimater
    Args:
        predict_number_func (function): etimated game function

    Returns:
        int: Mean tryes count
    """
    np.random.seed(seed_num)
    passes = np.random.randint(0, 101, size = (1000, ), dtype=int)
    tryes_counts = np.zeros((passes.size, ), dtype=int)
    
    for i in range(0, passes.size):
        tryes_counts[i] = predict_number_func(passes[i])
    
    return round(tryes_counts.mean())
        

if __name__ == '__main__':
    print(score_game(predict_number))


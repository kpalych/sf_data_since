"""
Game Predict Number v2
"""

import numpy as np

def predict_number(number: int) -> int:
    """
    Predict Number by Random method

    Args:
        number (int): destination number

    Returns:
        int: tryes count
    """
    
    try_coutn  = 0
    while True:
        try_coutn += 1
        cur_number = np.random.randint(1, 101)
        if cur_number == number:
            break
        
    return try_coutn

def score_game(predict_number_func, seed_num = 1) -> int:
    """
    Game algorythm estimater
    Args:
        predict_number_func (function): etimated game function

    Returns:
        int: Mean tryes count
    """
    np.random.seed(seed_num)
    passes = np.random.randint(1, 101, size = (1000, ))
    tryes_counts = np.zeros((passes.size, ))
    
    for i in range(0, passes.size):
        tryes_counts[i] = predict_number_func(passes[i])
    
    return int(tryes_counts.mean())
        

if __name__ == '__main__':
    print(score_game(predict_number))


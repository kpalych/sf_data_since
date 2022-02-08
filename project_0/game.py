"""
Game Predict Number
"""

import numpy as np

number = np.random.randint(1, 101)

try_count = 0

while True:
    try_count += 1
    predict_number = int(input("Predict Number: "))
    
    if predict_number > number:
        print("Less")
    elif predict_number < number:
        print("Greater")
    else:
        print(f"Yore are Win! Tryes Count is {try_count}")
        break
    



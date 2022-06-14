"""Игра угадай число.
Компьютер сам загадывает и угадывает число
"""

import numpy as np

def random_predict(number:int=1) -> int:
    """Угадываем число используя дихотомию с предварительным разделением диапазона

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
        
    count = 0
    min_number = 0 
    medium_number1 = 25 # задаем отрезки для ускорения поиска
    medium_number2 = 50
    medium_number3 = 75
    max_number = 100
    if number <= medium_number1:
            max_number =  medium_number1
    elif number <= medium_number2:
            max_number = medium_number2
            min_number = medium_number1
    elif number <= medium_number3:
            max_number = medium_number3
            min_number = medium_number2 
    else:
         max_number = 100
         min_number = medium_number3  

    while True:
        count += 1
        predit_number = round((min_number+max_number)/2) # предполагаемое число
            
        if predit_number > number:
            max_number = predit_number
        elif predit_number < number:
            min_number = predit_number
        else:
            break # выход из цикла, если угадали
    return(count)

print(f'Количество попыток: {random_predict()}')

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

#Run
if __name__ == '__main__':
    score_game (random_predict)
import numpy as np
def game_core_v3(number):
    """Функция для угадывания числа методом бинарного поиска. 
    Args:
        number (int): Загаданное число от 1 до 100  
    Returns:
        int: Количество попыток
    """
    count = 0
    left = 1
    right = 100
    while left <= right:
        count += 1
        predict = (left + right) // 2  # предполагаемое число - середина диапазона
        if predict == number:
            break  # выход из цикла, если угадали
        elif predict > number:
            right = predict - 1  # сужаем диапазон справа
        else:
            left = predict + 1   # сужаем диапазон слева   
    return count
def score_game(game_core):
    """Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число.  
    Args:
        game_core (function): Функция для угадывания числа   
    Returns:
        int: Среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED для воспроизводимости
    random_array = np.random.randint(1, 101, size=1000)
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score
# Запускаем тестирование
score_game(game_core_v3)
import numpy as np

def binary_search(number):
    '''Применим двоичный поиск в отсортированной последовательности'''
    random_array = np.random.randint(1, 101, size=(1000))
    random_array.sort()
    predict_num = np.random.randint(1, 101)
    middle = len(random_array) // 2
    first_element = 0
    last_element = len(random_array) - 1
   
    count = 1
    
    while random_array[middle] != predict_num:
        count+=1
        if predict_num > random_array[middle]:
            first_element = middle + 1
        else:
            last_element = middle - 1
        middle = (first_element + last_element) // 2
    return count

def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    return(f"Ваш алгоритм угадывает число в среднем за {score} попыток")

print(score_game(binary_search))







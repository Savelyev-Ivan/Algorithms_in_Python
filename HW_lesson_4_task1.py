# 1. Проанализировать скорость и сложность алгоритмов,
# разработанных в рамках домашнего задания из первых 3-х уроков
#  - Выберите любые 3 задачи
#  - Измерьте время работы вашего кода при помощи timeit и cProfile
#  - Результаты измерений сохрание в файл с кодом в виде комментариев
#  - При необходимости, измените исходный код

import random
import cProfile
import timeit

def max_below_zero(size):
    # SIZE = 10
    array = [random.randint(size * -10,size * 10) for _ in range(size)]
    # print(array)

    i = 0
    index = -1

    while i < size:
        if array[i] < 0 and index == -1:
            index = i
        elif array[i] < 0 and array[i] > array[index]:
            index = i

        i += 1
    # print(f'Число {array[index]} на позиции {index}')
    return f'Число {array[index]} на позиции {index}'

# "tested.max_below_zero(10)"
# 1000 loops, best of 5: 13.2 nsec per loop

# "tested.max_below_zero(100)"
# 1000 loops, best of 5: 128 nsec per loop

# "tested.max_below_zero(1000)"
# 1000 loops, best of 5: 1.37 msec per loop

# "tested.max_below_zero(10000)"
# 1000 loops, best of 5: 13.6 msec per loop



# cProfile.run('max_below_zero(1000)'
# # 5634 function calls in 0.002 seconds
#
#   Ordered by: standard name
#
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.002    0.002 <string>:1(<module>)
#        1    0.000    0.000    0.002    0.002 HW_lesson_4_task1.py:12(max_below_zero)
#        1    0.000    0.000    0.002    0.002 HW_lesson_4_task1.py:14(<listcomp>)
#     1000    0.001    0.000    0.001    0.000 random.py:200(randrange)
#     1000    0.000    0.000    0.002    0.000 random.py:244(randint)
#     1000    0.001    0.000    0.001    0.000 random.py:250(_randbelow_with_getrandbits)
#        1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
#     1000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#     1629    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}


#         cProfile.run('max_below_zero(1000)'
#         506 function calls in 0.000 seconds
#
#   Ordered by: standard name
#
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        1    0.000    0.000    0.000    0.000 HW_lesson_4_task1.py:12(max_below_zero)
#        1    0.000    0.000    0.000    0.000 HW_lesson_4_task1.py:14(<listcomp>)
#      100    0.000    0.000    0.000    0.000 random.py:200(randrange)
#      100    0.000    0.000    0.000    0.000 random.py:244(randint)
#      100    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#      100    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      101    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}



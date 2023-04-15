# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент 
# к заданному числу X. Пользователь в первой строке вводит натуральное число 
# N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. 
# Последняя строка содержит число X 

from random import randint

n = int(input('Введите размер списка: '))

rand_list = []

for i in range(n):
    rand_list.append(randint(0, 99))

print(*rand_list)

x = int(input('Введите число: '))

difference = abs(rand_list[0] - x)
difference_index = 0

for i in range(1, len(rand_list)):
    d = abs(rand_list[i] - x)
    if d < difference: 
        difference = d
        difference_index = i

print(f'Максимально близкий элемент {rand_list[difference_index]}')
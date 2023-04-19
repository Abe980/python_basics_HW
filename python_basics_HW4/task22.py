from random import randint


n = int(input('Введите размер первого списка: '))
m = int(input('Введите размер второго списка: '))


def get_list(size):
    my_list = []
    for i in range(size):
        my_list.append(randint(0, 9))
    return my_list


set1 = set(get_list(n))
set2 = set(get_list(m))
result = list(set1 & set2)


print(set1)
print(set2)

result.sort()
print(result)



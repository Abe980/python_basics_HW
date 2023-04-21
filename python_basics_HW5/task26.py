# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии


def get_degree(basis, degree):
    if degree >= 0:
        if degree == 0: return 1
        return basis * get_degree(basis, degree - 1)
    else:
        if degree == -1: return 1 / basis
        return (1 / basis) * (get_degree(basis, degree + 1))


basis = int(input('Введите основание степени: '))
degree = int(input('Введите степень: '))

print(get_degree(basis, degree) if (get_degree (basis, degree) - round(get_degree (basis, degree))) == 0 
      else f'{get_degree(basis, degree):.5}')

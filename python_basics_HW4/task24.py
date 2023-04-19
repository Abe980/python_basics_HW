from random import randint

my_list = []
result = []
count = int(input('Введите количество кустов: '))
for i in range(count):
  my_list.append(randint(1, 9))

print(my_list)


for i in range(len(my_list)):
  result.append(my_list[i - 2] + my_list[i - 1] + my_list[i])

print(result)
print(max(result))
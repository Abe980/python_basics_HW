# 1. Открывать файл (режим txt)+
# 2. Сохранить файл
# 3. Показать все контакты
# 4. Добавить контакт
# 5. Найти контакт
# 6. Изменить контакт
# 7. Удалить контакт
# 8. Выход


def open_file_read(path):
    with open(path,'r') as file:
        main_list=(file.readlines())   
        main_list_str=[x.rstrip().split(':') for x in main_list]
    return main_list_str
    

def open_file_write(path, list_file):
    with open(path, 'w') as file:
        file.writelines([':'.join(x)+'\n' for x in list_file])


def look_list(data_list):
    for elem in [' '.join(x) for x in data_list]: print(elem)
        

def add_contact(last_name, first_name, number, comment):
    data_list.append([last_name, first_name, number, comment])


def find_contact(data, data_list):
    res = []
    for cont in data_list:
        for dt in cont:
            if data == dt: 
                res.append(cont)
    return res


def edit_contact():
    data = input('Введите информацию о контакте: ')
    res_find = find_contact(data, data_list)
    for i in range(len(res_find)):
            print(f'{i+1} - {" ".join(res_find[i])}')
    contact = int(input('Введите номер контакта, который хотите изменить: '))
    data_edit = int(input('''
            Выберете информацию которую хотите изменить:
            1 - фамилию
            2 - имя
            3 - номер телефона
            4 - комментарий
        '''))
    new_info = input('Введите новую информацию: ')
    edit_list = res_find[contact-1]
    i1 = data_list.index(edit_list)
    data_list[i1][data_edit-1] = new_info

def del_contact():
    data = input('Введите информацию о контакте: ')
    res_find = find_contact(data, data_list)
    for i in range(len(res_find)):
            print(f'{i+1} - {" ".join(res_find[i])}')
    contact = int(input('Введите номер контакта, который хотите удалить: '))
    edit_list = res_find[contact-1]
    i1 = data_list.index(edit_list)
    data_list.pop(i1)
    print('Контакт удален')



path = 'python_basics_HW8\phone_book.txt'
data_list = open_file_read(path)
correct_input = True

while correct_input:
    user_input = input('''
        Выберете действие:
        1 - Показать все контакты
        2 - Добавить контакт
        3 - Найти контакт
        4 - Изменить контакт
        5 - Удалить контакт

        0 - Выход

    ''')
    if user_input == '1':
        look_list(data_list)
    elif user_input == '2':
        last_name = input('Введите фамилию: ')
        first_name = input('Введите имя: ')
        number = input('Введите номер телефона: ')
        comment = input('Введите комментарий: ')
        add_contact(last_name, first_name, number, comment)
        print(f'Контакт "{last_name} {first_name} {number} {comment}" добавлен')
    elif user_input == '3':
        data = input('Введите информацию для поиска: ')
        for elem in find_contact(data, data_list):
            print(' '.join(elem))
    elif user_input == '4':
        edit_contact()
    elif user_input == '5':
        del_contact()
    elif user_input == '0':
        open_file_write(path, data_list)
        break
    else:
        print('Не корректный ввод')

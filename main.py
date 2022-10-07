

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email


def commands():
    print("Команды: ")
    print("1 - Показать все контакты", "2 - Поиск по телефону", "3 - Поиск по почте", "4 - Поиск по ФИО",
          "5 - Показать контакты без номера или email", "6 - Изменение контакта", "7 - Завершить программу", sep="\n")


def print_data(data_base):
    for i in range(0, len(data_base[0])):
        string = 'ID = '+str(data_base[0][i]) + "\n"
        if data_base[1][i] != 'Отсутсвует':
            string += "ФИО = " + data_base[1][i]
        if data_base[2][i] != 'Отсутсвует':
            string += " " + data_base[2][i]
        if data_base[3][i] != 'Отсутсвует':
            string += " " + data_base[3][i]
        if data_base[4][i] != 'Отсутсвует':
            string += "\n" + "Номер телефона: " + data_base[4][i]
        else:
            string += "\n" + "Номер телефона отсутсвует "
        if data_base[5][i] != 'Отсутсвует':
            string += "\n" + "Почта: " + data_base[5][i] + "\n"
        else:
            string += "\n" + "Почта отсутсвует \n"
        print(string)


def print_data_1(data_base, id):
    string = 'ID = '+str(data_base[0][id]) + "\n"
    if data_base[1][id] != 'Отсутсвует':
        string += "ФИО = " + data_base[1][id]
    if data_base[2][id] != 'Отсутсвует':
        string += " " + data_base[2][id]
    if data_base[3][id] != 'Отсутсвует':
        string += " " + data_base[3][id]
    if data_base[4][id] != 'Отсутсвует':
        string += "\n" + "Номер телефона: " + data_base[4][id]
    else:
        string += "\n" + "Номер телефона отсутсвует "
    if data_base[5][id] != 'Отсутсвует':
        string += "\n" + "Почта: " + data_base[5][id] + "\n"
    else:
        string += "\n" + "Почта отсутсвует \n"
    print(string)


def add_new_contact(data_base, contact):
    data_base[0].append(len(data_base[0]) + 1)
    name = contact.name.split(" ")
    while len(name) < 3:
        name.append('Отсутсвует')
    data_base[1].append(name[0])
    data_base[2].append(name[1])
    data_base[3].append(name[2])
    if contact.phone != '':
        data_base[4].append(contact.phone)
    else:
        data_base[4].append('Отсутсвует')
    if contact.email != '':
        data_base[5].append(contact.email)
    else:
        data_base[5].append('Отсутсвует')
    return data_base


def search_by_phone(data_base, phone):
    if data_base[4].__contains__(phone):
        id = data_base[4].index(phone)
        print_data_1(data_base, id)
    else:
        print("Контакта с таким номером телефона нет")


def search_by_email(data_base, email):
    if data_base[5].__contains__(email):
        id = data_base[5].index(email)
        print_data_1(data_base, id)
    else:
        print('Контакта с таким Email нет')


def search_by_name(data_base, name):
    ids = []
    if name[0] != 'Отсутсвует':
        for i in range(len(data_base[1])):
            if name[0] == data_base[1][i]:
                ids.append(data_base[0][i] - 1)
    if name[1] != 'Отсутсвует':
        if name[0] != 'Отсутсвует':
            for id_ in ids:
                if name[1] != data_base[2][id_]:
                    ids.remove(id_)
        else:
            for i in range(len(data_base[2])):
                if name[1] == data_base[2][i]:
                    ids.append(data_base[0][i] - 1)
    if name[2] != 'Отсутсвует':
        if name[0] != 'Отсутсвует' or name[1] != 'Отсутсвует':
            for id_ in ids:
                if name[2] != data_base[3][id_]:
                    ids.remove(id_)
        else:
            for i in range(len(data_base[3])):
                if [2] == data_base[3][i]:
                    ids.append(data_base[0][i] - 1)
    if len(ids) == 0:
        print("Такого контакта не нашлось")
    else:
        for id_ in ids:
            print_data_1(data_base, id_)


def view_withot_smth(data_base, command_):
    if command_ == 1:
        for i in range(len(data_base[4])):
            if data_base[4][i] == "Отсутсвует":
                print_data_1(data_base, i)
        return
    if command_ == 2:
        for i in range(len(data_base[5])):
            if data_base[5][i] == "Отсутсвует":
                print_data_1(data_base, i)
        return
    if command_ == 3:
        for i in range(len(data_base[4])):
            if data_base[4][i] == "Отсутсвует" and data_base[5][i] == "Отсутсвует":
                print_data_1(data_base, i)
        return
    print("Не нашлось таких контактов")


print("Введите название файла")
file_name = input()
file = open(file_name, encoding='utf-8')
data_base = [[], [], [], [], [], []]
for s in file:
    string = s.split(",")
    contact = Contact(string[0], string[1].replace(" ", ""), string[2].replace(" ", "").replace("\n", ""))
    data_base = add_new_contact(data_base, contact)
print("Данные обработаны")
commands()
command = int(input())
while command != "hse_top!":
    if command == 1:
        print_data(data_base)
    elif command == 2:
        print("Введите номер телефона")
        phone = input()
        search_by_phone(data_base, phone)
    elif command == 3:
        print("Введите почту")
        email = input()
        search_by_email(data_base, email)
    elif command == 4:
        search_name = []
        print("Оставьте поле пустым, если не хотите искать по этому значению")
        print("Введите фамилию")
        surname = input()
        if surname != '':
            search_name.append(surname)
        else:
            search_name.append('Отсутсвует')
        print("Введите имя")
        name = input()
        if name != '':
            search_name.append(name)
        else:
            search_name.append('Отсутсвует')
        print("Введите отчество")
        fathers_name = input()
        if fathers_name != '':
            search_name.append(fathers_name)
        else:
            search_name.append('Отсутсвует')
        search_by_name(data_base, search_name)
    elif command == 5:
        print("Введите вид поиска: ", "1 - без номера", "2 - без почты", "3 - без обоих", sep="\n")
        command_ = int(input())
        view_withot_smth(data_base, command_)
    elif command == 6:
        print("Введите id контакта, данные о котором вы хотите изменить.")
        id_ = int(input())
        print('Что вы хотите изменить?', '1 - ФИО', '2 - Номер телефона', '3 - Email', '4 - Выйти из режима редактирования', sep='\n')
        command_ = int(input())
        while command_ != 'hse_top!':
            if command_ == 1:
                print('Введите новое ФИО через запятые(например, если вы хотите оставить фамилию пустой, то напишите так: Иван,, Иванович).')
                new_fio = (str(input())).split(",")
                for i in range(len(new_fio)):
                    new_fio[i].replace(' ', '')
                data_base[1][id_] = new_fio[0]
                data_base[2][id_] = new_fio[1]
                data_base[3][id_] = new_fio[2]
            if command_ == 2:
                print("Введите новый номер телефона.")
                new_phone = input()
                data_base[4][id_] = new_phone
            if command_ == 3:
                print("Введите новый Email.")
                new_email = input()
                data_base[5][id_] = new_email
            if command_ == 4:
                break
            print('Вы еще что-то хотите изменить?', '1 - ФИО', '2 - Номер телефона', '3 - Email',
                  '4 - Выйти из режима редактирования', sep='\n')
            command_ = int(input())

    elif command == 7:
        print("Программа выключена.")
        break
    commands()
    command = int(input())

# Дополнить справочник возможностью копирования данных из одного файла в другой.
# Пользователь вводит номер строки, которую необходимо перенести из одного файла в другой.

import os


def files_dir():
    print("Список файлов в рабочей директории")
    directory = os.getcwd()
    files = os.listdir(directory)
    print(*files, sep="\n")


def open_file(msg, param, data_list):
    if param == "r":
        files_dir()
        file_name = input("Введите имя файла телефонного справочника {}".format(msg))
        return read_txt(file_name)
    elif param == "a":
        file_name = input("Введите имя файла телефонного справочника {}".format(msg))
        return append_txt(file_name, data_list)


def print_phonebook(list_dict):
    print(
        "{:^10}{:15}{:10}{:10}{:10}".format(
            "Номер", "Фамилия", "Имя", "Телефон", "Описание"
        )
    )
    num = 0

    for dct in list_dict:
        num += 1
        print("{:^10}".format(num), end="")
        print("{:15}".format(dct["Фамилия"]), end="")
        print("{:10}".format(dct["Имя"]), end="")
        print("{:^10}".format(dct["Телефон"]), end="")
        print("{:10}".format(dct["Описание"]), end="")


def copy_user():
    list_in = open_file(" - из которого копируем ", "r", list())
    print_phonebook(list_in)
    print()
    num_str_copy = int(input("Номер строки которую надо скопировать "))
    open_file(" - в который копируем ", "a", list_in[num_str_copy - 1])
    # print_phonebook(list_out)
    # print(list_out(num_str_copy))


def find_by_lastname(phone_book, last_name):
    print("Данный раздел в разработке")


def change_number(phone_book, last_name, new_number):
    print("Данный раздел в разработке")


def delete_by_lastname(phone_book, lastname):
    print("Данный раздел в разработке")


def find_by_number(phone_book, number):
    print("Данный раздел в разработке")


def add_user(phone_book, user_data):
    print("Данный раздел в разработке")


def work_with_phonebook():
    choice = show_menu()

    while choice != 8:
        if choice == 1:
            print_phonebook(open_file("", "r", list()))
        elif choice == 2:
            last_name = input("lastname ")
            print(find_by_lastname(last_name))
        elif choice == 3:
            last_name = input("lastname ")
            new_number = input("new  number ")
            print(change_number(last_name, new_number))
        elif choice == 4:
            lastname = input("lastname ")
            print(delete_by_lastname(lastname))
        elif choice == 5:
            number = input("number ")
            print(find_by_number(number))
        elif choice == 6:
            user_data = input("new data ")
            add_user(user_data)
            write_txt("phonebook.txt")
        elif choice == 7:
            copy_user()

        choice = show_menu()


def show_menu():
    print(
        "\nВыберите необходимое действие:\n"
        "1. Отобразить весь справочник\n"
        "2. Найти абонента по фамилии\n"
        "3. Найти абонента по номеру телефона\n"
        "4. Добавить абонента в справочник\n"
        "5. изменить данные\n"
        "6. Сохранить справочник в текстовом формате\n"
        "7. Копирование данных в другой файл по номеру строки\n"
        "8. Завершение работы"
    )
    choice = int(input())
    return choice


def read_txt(filename):
    phone_book = []

    fields = ["Фамилия", "Имя", "Телефон", "Описание"]

    with open(filename, "r", encoding="utf-8") as phb:
        for line in phb:
            record = dict(zip(fields, line.split(",")))
            phone_book.append(record)

    return phone_book


def write_txt(filename, phone_book):
    with open("phonebook.txt", "w", encoding="utf-8") as phout:
        for i in range(len(phone_book)):
            s = ""
            for v in phone_book[i].values():
                s += v + ","
            phout.write(f"{s[:-1]}\n")


def append_txt(filename, append_str):
    with open(filename, "a", encoding="utf-8") as phapp:
        phapp.write("")
        s = ""
        for i in append_str.keys():
            s += append_str[i] + ","
        s.rstrip("\n")
        phapp.write(f"{s[:-1]}")


work_with_phonebook()

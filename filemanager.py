from victory import victory
from use_functions import bankfunc
import os

while True:
    print('1 - Создать папку\t\t\t\t', ' 7 - Просмотр информации об ОС')
    print('2 - Удалить файл/папку\t\t\t', ' 8 - Создатель программы')
    print('3 - Копировать файл/папку\t\t', ' 9 - Играть в викторину')
    print('4 - Просмотр рабочей директории\t', '10 - Мой банковский счёт')
    print('5 - Просмотреть только папки\t', '11 - ')
    print('6 - Просмотреть только файлы\t', '12 - Выход')
    print()
    choice = input('Выберите пункт меню: ')
    if choice == '1':  # Done
        folder = input('Введите название папки: ')
        if not os.path.exists(folder):
            os.mkdir(folder)
        print()
    elif choice == '2':
        pass
    elif choice == '3':
        pass
    elif choice == '4':  # Done
        print()
        print('Содержимое рабочей директории:')
        print(sorted(os.listdir()))
        print()
    elif choice == '5':
        pass
    elif choice == '6':
        pass
    elif choice == '7':
        pass
    elif choice == '8':  # Done
        print()
        print('Создатель программы: Ярослав С. Васильев,')
        print('студент Университета ИИ (2023)')
        print()
    elif choice == '9':  # Done
        victory()
    elif choice == '10':  # Done
        print()
        bankfunc()
    elif choice == '11':
        pass
    elif choice == '12':  # Done
        break
    else:
        print('Неверный пункт меню')
        print()

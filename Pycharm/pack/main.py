import sys

from display_people import display_people
from find_nomer import find_nomer
from get_person import get_person


def main():
    """
    Главная функция программы.
    """
    # Список людей.
    people = []

    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input("Введите команду >>> ").lower()

        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break

        elif command == 'add':
            # Запросить данные о человеке.
            person = get_person()

            # Добавить в словарь список.
            people.append(person)
            # Отсортировать список в случае необходимости.
            if len(people) > 1:
                people.sort(key=lambda item: item.get('d_bday', ''))

        elif command == 'list':
            # Отобразить всех людей.
            display_people(people)

        elif command == 'find':
            n = int(input('Введите номер телефона: '))

            # Выбрать людей с заданной фамилией.
            finded = find_nomer(people, n)
            # Отобразить выбранных работников.
            display_people(finded)

        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n"
                  "add - добавить человека;\n"
                  "list - вывести список людей;\n"
                  "find - найти человека по номеру телефона;\n"
                  "help - отобразить справку;\n"
                  "exit - завершить работу с программой.\n")

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)

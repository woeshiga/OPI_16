from datetime import datetime


def get_person():
    """"
    Запросить данные о человеке.
    """
    name = input("Фамилия Имя: ")
    number = int(input("Номер телефона: "))
    bday = list(map(int, input("Дата рождения: ").split('.')))
    d_bday = datetime(bday[2], bday[1], bday[0])

    # Создать словарь.
    return {
        'name': name,
        'number': number,
        'birthday': d_bday,
    }

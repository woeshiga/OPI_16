def display_people(staff):
    """
    Список данных о людях.
    """
    if staff:
        # Заголовок таблицы.
        line = '+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20,
            '-' * 14
        )
        print(line)
        print(
            '| {:^4} | {:^30} | {:^20} | {:^14} |'.format(
                "№",
                "Фамилия Имя",
                "Номер телефона",
                "Дата рождения"
            )
        )
        print(line)

        # Вывести данные о всех людях.
        for idx, person in enumerate(staff, 1):
            print(
                f'| {idx:>4} |'
                f' {person.get("name", ""):<30} |'
                f' {person.get("number", 0):<20} |'
                f' {person.get("birthday")}      |'
            )
        print(line)

    else:
        print("Результат не найден")
        
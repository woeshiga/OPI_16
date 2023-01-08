def find_nomer(staff, nomer):
    """
    Выбрать людей с заданным номером телефона.
    """
    # Сформировать список людей.
    result = []

    for n in staff:
        if nomer in n.values():
            result.append(n)

    # Проверка на наличие записей
    if len(result) == 0:
        return None

    # Возвратить список выбранных людей.
    return result

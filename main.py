import os

import numpy as np

from config import DATA_DIR
from src import utils, transactions, transactions_filter, processing, widget


def main():
    """Основная функция, которая формирует логику программы и связывает функциональности между собой"""

    operations_path_1 = os.path.join(DATA_DIR, "operations.json")
    operations_path_2 = os.path.join(DATA_DIR, "transactions.csv")
    operations_path_3 = os.path.join(DATA_DIR, "transactions_excel.xlsx")

    print(
        "Программа: Привет! Добро пожаловать в программу работы \nс "
        "банковскими транзакциями.\nВыберите необходимый пункт меню:"
        "\n1. Получить информацию о транзакциях из JSON-файла"
        "\n2. Получить информацию о транзакциях из CSV-файла"
        "\n3. Получить информацию о транзакциях из XLSX-файла"
    )
    file_type = str(input("Выбрать пункт: "))

    # Блок выбора файла для анализа
    while file_type not in ["1", "2", "3"]:
        print("Введите цифру от 1 до 3")
        file_type = str(input("Выбрать пункт: "))

    if file_type == "1":
        file_choise = utils.read_transactions_json(operations_path_1)
        print("Для обработки выбран JSON-файл.")
    elif file_type == "2":
        file_choise = transactions.read_transactions_csv(operations_path_2)
        print("Для обработки выбран CSV-файл.")
    elif file_type == "3":
        file_choise = transactions.read_transactions_excel(operations_path_3)
        print("Для обработки выбран  EXSEL-файл.")

    # Блок выбора статуса операции
    print(
        "Введите статус, по которому необходимо выполнить фильтрацию. "
        "\nДоступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"
    )
    status_operation_user = (str(input("Ввести статус: "))).upper()
    while status_operation_user not in ["EXECUTED", "CANCELED", "PENDING"]:
        print(f"Статус операции {status_operation_user} недоступен.")
        print(
            "Введите статус, по которому необходимо выполнить фильтрацию. "
            "\nДоступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"
        )
        status_operation_user = (str(input("Ввести статус: "))).upper()

    result_filter = processing.filter_by_state(file_choise, status_operation_user)

    # Блок фильтрации в соответствии с выбором пользователя
    print("Отсортировать операции по дате? Да/Нет")
    sort_date_user = str(input("Ответ: ")).title()
    while sort_date_user not in ["Да", "Нет", "Yes", "No"]:
        print(f"Введенный ответ {sort_date_user} не соответствует возможным вариантам")
        print("Отсортировать операции по дате? Да/Нет")
        sort_date_user = str(input("Ответ: ")).title()
    if sort_date_user in ["Да", "Yes"]:
        print("Отсортировать по возрастанию или по убыванию? ")
        sort_date_direction = str(input("Ответ: ")).lower()
        while sort_date_direction not in ["по возрастанию", "по убыванию"]:
            print(f"Введенный ответ {sort_date_direction} не соответствует возможным вариантам")
            print("Отсортировать по возрастанию или по убыванию? ")
            sort_date_direction = str(input("Ответ: ")).lower()
        if sort_date_direction == "по убыванию":
            result_filter = processing.sort_by_date(result_filter)
        else:
            sort_date_direction = False
            result_filter = processing.sort_by_date(result_filter, sort_date_direction)

    print("Выводить только рублевые тразакции? Да/Нет")
    currency_user = str(input("Ответ: ")).title()
    while currency_user not in ["Да", "Нет", "Yes", "No"]:
        print(f"Введенный ответ {currency_user} не соответствует возможным вариантам")
        print("Выводить только рублевые тразакции? Да/Нет")
        currency_user = str(input("Ответ: ")).title()
    if currency_user in ["Да", "Yes"]:
        currency_user = "RUB"
        result_filter = transactions_filter.filter_by_currency(result_filter, currency_user)

    print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
    description_user = str(input("Ответ: ")).title()
    while description_user not in ["Да", "Нет", "Yes", "No"]:
        print(f"Введенный ответ {description_user} не соответствует возможным вариантам")
        print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
        description_user = str(input("Ответ: ")).title()
    if description_user in ["Да", "Yes"]:
        string_user = str(input("Введите слово для поиска: ")).lower()
        result_filter = transactions_filter.search_string(result_filter, string_user)

    print("Распечатываю итоговый список транзакций...")
    print(f"Всего банковских операций в выборке: {len(result_filter)}")

    # Назначение маски для номеров карт и банковских счетов
    for operation in result_filter:
        original_date = operation["date"]
        if "from" in operation and operation["from"]:
            if not isinstance(operation["from"], float) or not np.isnan(operation["from"]):
                operation["from"] = widget.mask_account_card(operation["from"])
        if "to" in operation:
            operation["to"] = widget.mask_account_card(operation["to"])
        operation["date"] = widget.get_date(original_date)
    print(result_filter)
    if len(result_filter) != 0:
        first_item = result_filter[0]
        for operation in result_filter:
            if "currency_name" in first_item and "from" in first_item and "to" in first_item:
                print(
                    f"{operation['date']} {operation['description']} "
                    f"\n{operation['from']} -> {operation['to']} "
                    f"\nСумма: {operation['amount']} {operation['currency_name']}\n"
                )
            elif "operationAmount" in first_item and "from" in first_item and "to" in first_item:
                print(
                    f"{operation['date']} {operation['description']} "
                    f"\n{operation.get('from')} -> {operation['to']} "
                    f"\nСумма: {operation['operationAmount']['amount']} "
                    f"{operation['operationAmount']['currency']['name']}\n"
                )
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")


if __name__ == "__main__":
    main()

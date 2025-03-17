import os
from config import DATA_DIR
from src import utils, transactions, transactions_filter, processing


def main():
    """Основная функция, которая формирует логику программы и связывает функциональности между собой """

    operations_path_1 = os.path.join(DATA_DIR, "operations.json")
    operations_path_2 = os.path.join(DATA_DIR, "transactions.csv")
    operations_path_3 = os.path.join(DATA_DIR, "transactions_excel.xlsx")

    print(
        "Программа: Привет! Добро пожаловать в программу работы \nс банковскими транзакциями.\nВыберите необходимый пункт меню:\n1. Получить информацию о транзакциях из JSON-файла\n2. Получить информацию о транзакциях из CSV-файла\n3. Получить информацию о транзакциях из XLSX-файла"
    )
    file_type = str(input("Выбрать пункт: "))

    # Блок выбора файла для анализа
    while file_type not in ["1", "2", "3"]:
        print("Введите цифру от 1 до 3")
        file_type = str(input("Выбрать пункт: "))

    if file_type == "1":
        file_choise = utils.read_transactions_json(operations_path_1)
        print("Для обработки выбран JSON-файл.")
        # print(file_choise)
    elif file_type == "2":
        file_choise = transactions.read_transactions_csv(operations_path_2)
        print("Для обработки выбран CSV-файл.")
        # print(file_choise)
    elif file_type == "3":
        file_choise = transactions.read_transactions_excel(operations_path_3)
        print("Для обработки выбран  EXSEL-файл.")
        # print(file_choise)

    # Блок выбора статуса операции
    print(
        "Введите статус, по которому необходимо выполнить фильтрацию. \nДоступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"
    )
    status_operation_user = (str(input("Ввести статус: "))).upper()
    while status_operation_user not in ["EXECUTED", "CANCELED", "PENDING"]:
        print(f"Статус операции {status_operation_user} недоступен.")
        print(
            "Введите статус, по которому необходимо выполнить фильтрацию. \nДоступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"
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
            sort_date_direction = str(input("Ответ: ")).lower()
        if sort_date_direction == "по убыванию":
            sort_date = processing.sort_by_date(result_filter)
        else:
            sort_date_direction = False
            sort_date = processing.sort_by_date(result_filter, sort_date_direction)
    elif sort_date_user in ["Нет", "No"]:
        sort_date = result_filter

    print("Выводить только рублевые тразакции? Да/Нет")
    currency_user = str(input("Ответ: ")).lower()
    while currency_user not in ["Да", "Нет", "Yes", "No"]:
        print(f"Введенный ответ {currency_user} не соответствует возможным вариантам")
        print("Выводить только рублевые тразакции? Да/Нет")
        currency_user = str(input("Ответ: ")).title()


if __name__ == "__main__":
    print(main())

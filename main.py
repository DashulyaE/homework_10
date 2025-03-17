import os
from config import DATA_DIR
from src import utils, transactions


def main():
    operations_path = os.path.join(DATA_DIR, "operations.json")
    print(
        "Программа: Привет! Добро пожаловать в программу работы \nс банковскими транзакциями.\nВыберите необходимый пункт меню:\n1. Получить информацию о транзакциях из JSON-файла\n2. Получить информацию о транзакциях из CSV-файла\n3. Получить информацию о транзакциях из XLSX-файла"
    )
    file_type = str(input("Выбрать пункт: "))
    while file_type not in ["1", "2", "3"]:
        print("Введите цифру от 1 до 3")
        file_type = str(input("Выбрать пункт: "))

    if file_type == "1":
        operations_path = os.path.join(DATA_DIR, "operations.json")
        file_choise = utils.read_transactions_json(operations_path)
        print("Для обработки выбран JSON-файл.")
        # print(file_choise)
    elif file_type == "2":
        operations_path = os.path.join(DATA_DIR, "transactions.csv")
        file_choise = transactions.read_transactions_csv(operations_path)
        print("Для обработки выбран CSV-файл.")
        # print(file_choise)
    elif file_type == "3":
        operations_path = os.path.join(DATA_DIR, "transactions_excel.xlsx")
        file_choise = transactions.read_transactions_excel(operations_path)
        print("Для обработки выбран  EXSEL-файл.")
        # print(file_choise)

    print(
        "Введите статус, по которому необходимо выполнить фильтрацию. \nДоступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"
    )
    status_operation = (str(input("Ввести статус: "))).upper()
    while status_operation not in ["EXECUTED", "CANCELED", "PENDING"]:
        print(f"Статус операции {status_operation} недоступен.")
        print(
            "Введите статус, по которому необходимо выполнить фильтрацию. \nДоступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"
        )
        status_operation = (str(input("Ввести статус: "))).upper()


if __name__ == "__main__":
    print(main())

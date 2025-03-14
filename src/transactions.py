import csv
import os


rows = []
def read_transactions_csv(operations_path: str) -> list[dict]:
    """Функция считывания финансовых операций из CSV, выдает список словарей с транзакциями"""

    if os.path.exists(operations_path):
        with open(operations_path, "r", encoding="UTF-8") as file:
            reader = csv.DictReader(file, delimiter=';')
            for row in reader:
                rows.append(row)
                #return (row['id'], row['state'], row['date'], row['amount'], row['currency_name'], row['currency_code'], row['from'], row['to'], row['description'])
            if rows == []:
                print('Файл пустой или не верно заполнен')
                return rows
            else:
                return rows
    else:
        print('Путь к файлу или файл не найден')
        return rows


def read_transactions_excel():

    pass

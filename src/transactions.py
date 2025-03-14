import csv
import pandas as pd


def read_transactions_csv(operations_path):
    """Функция считывания финансовых операций из CSV, выдает список словарей с транзакциями"""

    rows = []
    try:
        with open(operations_path, "r", encoding="UTF-8") as file:
            reader = csv.DictReader(file, delimiter=";")
            for row in reader:
                rows.append(row)
            if rows == []:
                return "Файл пустой или не верно заполнен"
            else:
                return rows
    except Exception as e:
        return f"Файл не найден, пустой или не верно заполнен. Ошибка: {e}"


def read_transactions_excel(operations_path_ex):
    """Функция считывания финансовых операций из exsel, выдает список словарей с транзакциями"""

    try:
        excel_data = pd.read_excel(operations_path_ex)
        return excel_data.to_dict(orient="records")
    except Exception as e:
        return f"Файл не найден, пустой или не верно заполнен. Ошибка: {e}"

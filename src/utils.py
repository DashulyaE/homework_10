import json
import os

new_dir = os.chdir("..")


def read_transactions_json(relative_path):
    """Функция чтения JSON-файла с информацией о транзакиях"""

    null_json = []
    absolute_path = os.path.abspath(relative_path)
    if os.path.exists(absolute_path):
        with open(absolute_path, "r", encoding="UTF-8") as f:
            try:
                data = json.load(f)
                return data
            except ValueError:
                return null_json
    else:
        return null_json


relative_path = "data/operations.json"
print(read_transactions_json(relative_path))

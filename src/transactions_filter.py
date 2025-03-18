import re
from collections import Counter


def search_string(my_list_dict: list[dict], my_string: str) -> list[dict]:
    """Функция поиска строки из поля description в списке словарей с транзакциями"""
    result = []
    pattern = re.compile(my_string, flags=re.IGNORECASE)
    for i in my_list_dict:
        if "description" in i and pattern.findall(i["description"]):
            result.append(i)
    return result


def category_count(my_list_dict: list[dict], my_descriptions: list) -> dict:
    """Функция подсчета категорий банковских операций"""

    result = {}
    my_category = [transaction["description"] for transaction in my_list_dict]
    print(my_category)
    count_operations = Counter(my_category)
    for i in my_descriptions:
        result[i] = count_operations[i]
    return result


def filter_by_currency(log_operation: list[dict], currency: str = "RUB") -> list[dict]:
    """Функция фильтрации банковских операций по значению ключа state"""
    selected_operation = []
    if isinstance(log_operation, list) and len(log_operation) > 0:
        first_item = log_operation[0]
        if 'currency_name' in first_item and 'from' in first_item and 'to' in first_item:
            for operation in log_operation:
                if operation["currency_code"] == currency:
                    selected_operation.append(operation)
        elif 'operationAmount' in first_item and 'from' in first_item and 'to' in first_item:
            for operation in log_operation:
                if operation["operationAmount"]["currency"]["code"] == currency:
                    selected_operation.append(operation)
    return selected_operation


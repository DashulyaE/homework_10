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

def filter_by_state(log_operation: list[dict], choose_state: str = "EXECUTED") -> list[dict]:
    """Функция фильтрации банковских операций по значению ключа state"""
    selected_operation = []
    for operation in log_operation:
        if operation.get("state") == choose_state:
            selected_operation.append(operation)
    return selected_operation


def sort_by_date(log_operation: list[dict], sort_date: bool = True) -> list[dict]:
    """Функция сортировки банковских операций по дате создания"""
    sorted_operation = sorted(log_operation, key=lambda x: x["date"], reverse=sort_date)
    return sorted_operation

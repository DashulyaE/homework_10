def filter_by_state(log_operation: list[dict], choose_state: str = "EXECUTED") -> list[dict]:
    """Создание функции фильтрации банковских операций по значению ключа state"""
    selected_operation = []
    for operation in log_operation:
        if operation.get("state") == choose_state:
            selected_operation.append(operation)
    return selected_operation

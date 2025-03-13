import json
import os
import logging
from config import LOGS_DIR


log_file_path = os.path.join(LOGS_DIR, "utils.log")
file_logger = logging.getLogger("utils")
file_handler = logging.FileHandler(log_file_path, encoding="utf-8", mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
file_logger.addHandler(file_handler)
file_logger.setLevel(logging.DEBUG)


def read_transactions_json(operations_path):
    """Функция чтения JSON-файла с информацией о транзакиях"""

    null_json = []
    if os.path.exists(operations_path):
        file_logger.info("Путь к файлу успешно найден")
        with open(operations_path, "r", encoding="UTF-8") as f:
            try:
                data = json.load(f)
                # file_logger.info("JSON файл успешно загружен")
                return data
            except ValueError as e:
                file_logger.error(f"Ошибка: {e}")
                return null_json
    else:
        file_logger.error("Путь к JSON файлу или файл не найден")
        return null_json

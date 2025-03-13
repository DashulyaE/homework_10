import os
import logging
from config import LOGS_DIR


log_file_path = os.path.join(LOGS_DIR, "masks.log")
file_logger = logging.getLogger("masks")
file_handler = logging.FileHandler(log_file_path, encoding="utf-8", mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s – %(funcName)s – %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
file_logger.addHandler(file_handler)
file_logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: str) -> str:
    """Функция, которая маскирует номер банковской карты"""
    if len(card_number) == 16:
        if card_number.isdigit():
            mask_number = card_number[:4] + " " + card_number[4:6] + "** **** " + card_number[12:]
            file_logger.info("Успешно выполнено создание маски для банковской карты")
            return mask_number
        else:
            file_logger.error(f"Ошибка при вводе счета: {card_number}")
            raise ValueError("Номер карты должен состоять из цифр")
    else:
        file_logger.error(f"Ошибка длины номера карты: {card_number}")
        raise ValueError("Номер карты должен состоять из 16 цифр")


def get_mask_account(bank_account: str) -> str:
    """Функция, которая маскирует номер банковского счета"""
    if len(bank_account) == 20:
        if bank_account.isdigit():
            mask_account = "**" + bank_account[-4:]
            file_logger.info("Успешно выполнено создание маски для банковского счета")
            return mask_account
        else:
            file_logger.error(f"Ошибка при вводе счета: {bank_account}")
            raise ValueError("Номер счета должен состоять из цифр")
    else:
        file_logger.error(f"Ошибка длины номера счета: {bank_account}")
        raise ValueError("Номер счета должен состоять из 20 цифр")

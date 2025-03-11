import logging
import os

new_dir = os.chdir("..")

# Настройка логирования
card_logger = logging.getLogger("masks.mask_card")
account_logger = logging.getLogger("masks.mask_account")

file_handler = logging.FileHandler("logs/masks.log", encoding="utf-8", mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
card_logger.addHandler(file_handler)
account_logger.addHandler(file_handler)
card_logger.setLevel(logging.DEBUG)
account_logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: str) -> str:
    """Функция, которая маскирует номер банковской карты"""
    if len(card_number) == 16:
        if card_number.isdigit():
            mask_number = card_number[:4] + " " + card_number[4:6] + "** **** " + card_number[12:]
            card_logger.info("Успешно выполнено создание маски для банковской карты")
            return mask_number
        else:
            card_logger.error(f"Ошибка при вводе счета: {card_number}")
            raise ValueError("Номер карты должен состоять из цифр")
    else:
        card_logger.error(f"Ошибка длины номера карты: {card_number}")
        raise ValueError("Номер карты должен состоять из 16 цифр")


def get_mask_account(bank_account: str) -> str:
    """Функция, которая маскирует номер банковского счета"""
    if len(bank_account) == 20:
        if bank_account.isdigit():
            mask_account = "**" + bank_account[-4:]
            account_logger.info("Успешно выполнено создание маски для банковского счета")
            return mask_account
        else:
            account_logger.error(f"Ошибка при вводе счета: {bank_account}")
            raise ValueError("Номер счета должен состоять из цифр")
    else:
        account_logger.error(f"Ошибка длины номера счета: {bank_account}")
        raise ValueError("Номер счета должен состоять из 20 цифр")


if __name__ == "__main__":
    print(get_mask_card_number("1596837868705199"))
    print(get_mask_account("73654jj1430135874305"))

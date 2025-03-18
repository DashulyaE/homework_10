from datetime import datetime
from src import masks
from src.masks import get_mask_account


def mask_account_card(bank_info: str) -> str:
    """Функция, которая маскирует банковский счет, либо номер банковской карты"""
    number_card = ""
    for i in reversed(bank_info):
        if i.isdigit():
            number_card += i
        elif i.isalpha() or i == " ":
            break

    name_end = len(bank_info) - len(number_card)
    number_card = number_card[::-1]
    name_card = bank_info[: name_end - 1]
    if len(number_card) == 16:
        mask_card = name_card + " " + masks.get_mask_card_number(number_card)
        return mask_card
    elif len(number_card) == 20:
        mask_card = name_card + " " + masks.get_mask_account(number_card)
        return mask_card
    else:
        raise ValueError("Проверьте правильность счета(карта - 16 цифр, счет - 20 цифр)")


def get_date(date_user: str) -> str:
    """Функция, которая преобразует формат введенной даты пользователем"""
    if date_user != "":
        try:
            date_obj = datetime.strptime(date_user, "%Y-%m-%dT%H:%M:%S.%f")
        except ValueError:
            date_obj = datetime.strptime(date_user, "%Y-%m-%dT%H:%M:%SZ")
        return date_obj.strftime("%d.%m.%Y")

    else:
        raise ValueError("Поле ввода пусто")
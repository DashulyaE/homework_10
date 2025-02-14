from datetime import datetime

from src import masks


def mask_account_card(bank_info: str) -> str:
    """Функция, которая маскирует банковский счет, либо номер банковской карты"""
    naim_card = ""
    number_card = ""
    mask_card = ""

    for i in bank_info:
        if i.isalpha():
            naim_card += i
        if i == " ":
            naim_card += " "
        if i.isdigit():
            number_card += i


    if len(number_card) == 16:
        mask_card = naim_card + " " + masks.get_mask_card_number(number_card)
        return mask_card
    elif len(number_card) == 20:
        mask_card = naim_card + " " + masks.get_mask_account(number_card)
        return mask_card
    else:
        return "Проверьте правильность счета(карта - 16 цифр, счет - 20 цифр)"


def get_date(date_user: str) -> str:
    """Функция, которая преобразует формат введенной даты пользователем"""
    date_obj = datetime.strptime(date_user, "%Y-%m-%dT%H:%M:%S.%f")
    return date_obj.strftime("%d.%m.%Y")

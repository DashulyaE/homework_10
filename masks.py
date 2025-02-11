def get_mask_card_number(card_number: str) -> str:
    """Функция, которая маскирует номер банковской карты"""
    mask_number = card_number[:4] + " " + card_number[4:6] + "** **** " + card_number[12:]
    return mask_number


def get_mask_account(bank_account: str) -> str:
    """Функция, которая маскирует номер банковского счета"""
    mask_account = "**" + bank_account[-4:]
    return mask_account

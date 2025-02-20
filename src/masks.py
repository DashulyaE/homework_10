def get_mask_card_number(card_number: str) -> str:
    """Функция, которая маскирует номер банковской карты"""
    if len(card_number) == 16:
        if card_number.isdigit():
            mask_number = card_number[:4] + " " + card_number[4:6] + "** **** " + card_number[12:]
            return mask_number
        else:
            raise ValueError("Номер карты должен состоять из цифр")
    else:
        raise ValueError("Номер карты должен состоять из 16 цифр")


def get_mask_account(bank_account: str) -> str:
    """Функция, которая маскирует номер банковского счета"""
    if len(bank_account) == 20:
        if bank_account.isdigit():
            mask_account = "**" + bank_account[-4:]
            return mask_account
        else:
            raise ValueError("Номер счета должен состоять из цифр")
    else:
        raise ValueError("Номер счета должен состоять из 20 цифр")

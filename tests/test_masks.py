from src.masks import get_mask_card_number
from src.masks import  get_mask_account


def test_get_mask_card_number(card_number):
    """Функция проверки правильной маскировки номера карты """
    assert get_mask_card_number('1596837868705199')== card_number


def  test_get_mask_card_number(len_card):
    assert get_mask_card_number(len(len_card)) == len_card


def test_get_mask_account(account_bank):
    """Функция проверки правильной маскировки номера банковского счета """
    assert get_mask_account('64686473678894779589') == account_bank


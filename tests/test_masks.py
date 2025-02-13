from src.masks import get_mask_card_number
from src.masks import  get_mask_account

def test_get_mask_card_number(card_number):
    assert get_mask_card_number('1596837868705199')== card_number


def test_get_mask_account():
    assert get_mask_account('64686473678894779589') == '**9589'
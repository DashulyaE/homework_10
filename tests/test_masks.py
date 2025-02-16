from src.masks import get_mask_card_number, get_mask_account
import pytest


def test_get_mask_card_number(card_number: str) -> None:
    """Функция проверки на ошибку при вводе строки не равной 16 символам и вводе строки,
    состоящей не из одних цифр, правильной маскировки номера счета"""
    with pytest.raises(ValueError):
        get_mask_card_number("159683786870519а")

    with pytest.raises(ValueError):
        len(get_mask_card_number("1256"))

    assert get_mask_card_number(card_number) == "1596 83** **** 5199"


def test_get_mask_account(account_number: str) -> None:
    """Функция проверки на ошибку при вводе строки не равной 20 символам, вводе строки,
    состоящей не из одних цифр, правильной маскировки номера счета"""
    with pytest.raises(ValueError):
        get_mask_account("abcdabcdabcdabcdabcd")

    with pytest.raises(ValueError):
        len(get_mask_account("1256"))

    assert get_mask_account(account_number) == "**9589"

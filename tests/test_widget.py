from src.widget import mask_account_card, get_date
import pytest


@pytest.mark.parametrize(
    "account, mask",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account_card(account, mask):
    with pytest.raises(ValueError):
        len(mask_account_card("Maestro 1596837"))

    assert mask_account_card(account) == mask


@pytest.mark.parametrize(
    "user_date, format_date",
    [("2024-03-11T02:26:18.671407", "11.03.2024"), ("2023-10-09T03:15:18.671409", "09.10.2023")],
)
def test_get_date(user_date, format_date):

    with pytest.raises(ValueError):
        get_date("")

    with pytest.raises(ValueError):
        get_date("ffff")

    assert get_date(user_date) == format_date

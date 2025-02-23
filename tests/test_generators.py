from src.generators import filter_by_currency, transaction_descriptions, card_number_generator
import pytest


def test_filter_by_currency(transactions: list[dict]) -> None:
    generator1 = filter_by_currency(transactions, "")
    generator2 = filter_by_currency(transactions, "лаалал")
    generator3 = filter_by_currency(transactions, "USD")

    with pytest.raises(ValueError):
        next(generator1)

    with pytest.raises(ValueError):
        next(generator2)

    assert next(generator3) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
    assert next(generator3) == {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }


def test_transaction_descriptions(transactions: list[dict]) -> None:

    generator = transaction_descriptions(transactions)
    assert next(generator) == "Перевод организации"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == ""


@pytest.mark.parametrize("start, stop, result", [(2, 4, "0000 0000 0000 0002"), (3, 4, "0000 0000 0000 0003")])
def test_card_number_generator(start: int, stop: int, result: str) -> None:
    generator = card_number_generator(start, stop)
    generator2 = card_number_generator(0, 19999999999999999)

    assert next(generator) == result

    with pytest.raises(ValueError):
        next(generator2)

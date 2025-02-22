from collections.abc import generator
from locale import currency
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator
import pytest


def test_filter_by_currency(transactions):
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
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
    }
    assert next(generator3) == {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {
            "amount": "79114.93",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188"
    }
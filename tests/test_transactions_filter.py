from src.transactions_filter import search_string, category_count, filter_by_currency


def test_search_string(transactions: list[dict], my_string: str) -> list[dict]:
    assert search_string(transactions, my_string) == [
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        }
    ]


def test_category_count(transactions: list[dict], my_descriptions_list: list) -> dict:
    assert category_count(transactions, my_descriptions_list) == {
        "Перевод организации": 2,
        "Перевод с карты на карту": 1,
    }


def test_filter_by_currency(transactions: list[dict], transactions_res) -> list[dict]:
    assert filter_by_currency(transactions) == transactions_res

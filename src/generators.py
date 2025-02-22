from black import Iterator


def filter_by_currency(transactions: list[dict], currency: str = "USD") -> Iterator[dict]:
    currency = currency.upper()
    if currency in ["USD", "RUB"]:
        for item in transactions:
            if item["operationAmount"]["currency"]["code"] == currency:
                yield item
    elif currency == "":
        raise ValueError("Введите валюту")
    else:
        raise ValueError("Введите верный тип валюты")


def transaction_descriptions(transactions: list[dict]) -> Iterator[str]:
    for item in transactions:
        yield item["description"]


def card_number_generator():
    pass
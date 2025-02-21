from black import Iterator


def filter_by_currency(transactions: list[dict], currency: str = "USD") -> Iterator[dict]:
    for item in transactions:
        if item["operationAmount"]["currency"]["code"] == currency:
            yield item


def transaction_descriptions():
    pass


def card_number_generator():
    pass
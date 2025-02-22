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


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    if start >= 1 and start <= stop and stop <= 9999999999999999:
        card_numbers='0000000000000000'
        for card_number in range(start, stop + 1):
            card_number_gen = card_numbers[:-len(str(card_number))]+str(card_number)
            card_number_form = card_number_gen[:4] + " " + card_number_gen[4:8] + " " + card_number_gen[8:12] + " " + card_number_gen[12:]
            yield card_number_form
    else:
        raise ValueError("Номер карты не в заданном диапазоне")
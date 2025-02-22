from collections.abc import generator

from src.processing import filter_by_state, sort_by_date
from src import widget
from src import generators

choose_state = "CANCELED"
sort_date = False
log_operation = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-141T08:21:33.41944"},
]

transactions = [
        {
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
        },
        {
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
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
]

if __name__ == "__main__":
    #print(filter_by_state(log_operation, choose_state))
    #print(sort_by_date(log_operation, sort_date))
    #bank_info = input("Введите информацию о банковском счете/карте: ")
    #date_user = input("Введите дату ")
    #currency_user = (input("Введите валюту (USD, RUB): ")).upper()
    #print(f"Маска: {widget.mask_account_card(bank_info)}")
    #print(f"Новый формат даты: {widget.get_date(date_user)}")

    #if currency_user == "USD" or currency_user == "RUB":
    #currency_user = "USD"
    #usd_transactions = generators.filter_by_currency(transactions, currency_user)
    #for _ in range(5):
       # print(next(usd_transactions))
    #elif currency_user == '':
        #print('Вы не выбрали тип валюты')
    #else:
        #print('Выберите верный тип валюты')

    descriptions = generators.transaction_descriptions(transactions)
    for _ in range(6):
        print(next(descriptions))
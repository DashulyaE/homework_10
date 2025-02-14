from src.processing import filter_by_state, sort_by_date
from src import widget

choose_state = "CANCELED"
sort_date = False
log_operation = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

if __name__ == "__main__":
    print(filter_by_state(log_operation, choose_state))
    print(sort_by_date(log_operation, sort_date))


bank_info = input("Введите информацию о банковском счете/карте: ")
date_user = input("Введите дату ")

print(f"Маска: {widget.mask_account_card(bank_info)}")

if len(date_user) != 26:
    print("Неверный формат даты")
else:
    print(f"Новый формат даты: {widget.get_date(date_user)}")


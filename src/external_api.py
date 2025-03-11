import os
import requests
from dotenv import load_dotenv
from src.utils import read_transactions_json

load_dotenv()

API_KEY = os.getenv("API_KEY")
url = "https://api.apilayer.com/exchangerates_data/convert"


def currency_conversion(transaction_list: dict) -> float:
    """Функция, которая принимает на вход транзакцию и возвращает сумму транзакции в рублях"""

    amount = transaction_list.get("operationAmount", {}).get("amount")
    currency = transaction_list.get("operationAmount", {}).get("currency", {}).get("code")
    payload = {"amount": amount, "from": currency, "to": "RUB"}
    headers = {"apikey": API_KEY}

    if currency == "RUB":
        conversion = transaction_list.get("operationAmount", {}).get("amount", {})
        return conversion
    elif currency in ["USD", "EUR"]:
        try:
            response = requests.get(url, headers=headers, params=payload)
            if response.status_code == 200:
                result_answer = response.json()
                return float(result_answer["result"])
            else:
                print(f"Ошибка конвертации валюты: {response.status_code}")
                return 0.0
        except requests.exceptions.RequestException as e:
            print(f"Ошибка конвертации: {e}")
            return 0.0


relative_path = "data/operations.json"
transaction_list = read_transactions_json(relative_path)
# print(currency_conversion(transaction_list[0]))

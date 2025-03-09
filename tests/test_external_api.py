from unittest.mock import patch

import requests

from src.external_api import currency_conversion


@patch("src.external_api.requests.get")
def test_currency_conversion(mocked_get, transaction_usd, transaction_rub):

    assert currency_conversion(transaction_rub) == "67314.70"

    mocked_get.return_value.status_code = 200
    mocked_get.return_value.json.return_value = {
        "success": True,
        "query": {"from": "USD", "to": "RUB", "amount": 8221.37},
        "info": {"timestamp": 1741486023, "rate": 89.050893},
        "date": "2025-03-09",
        "result": 732120.340183,
    }
    expected_result = 732120.340183
    assert currency_conversion(transaction_usd) == float(expected_result)

    mocked_get.return_value.status_code = 524
    assert currency_conversion(transaction_usd) == 0.0


@patch("src.external_api.requests.get", side_effect=requests.exceptions.ConnectionError)
def test_currency_converter_failed_request(mock_get, transaction_usd):
    mock_get.side_effect = requests.exceptions.RequestException("Network error")
    assert currency_conversion(transaction_usd) == 0.0

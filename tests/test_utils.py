import json

from unittest import mock
from src.utils import read_transactions_json


def test_read_transactions_json():
    with mock.patch("os.path.exists", return_value=False):
        result = read_transactions_json("data/operations.json")
        assert result == []

    mock_json_data = [{"id": 1, "amount": 100}]
    with (
        mock.patch("os.path.exists", return_value=True),
        mock.patch("builtins.open", mock.mock_open(read_data=json.dumps(mock_json_data))),
    ):
        result = read_transactions_json("data/operations.json")
        assert result == mock_json_data

    with (
        mock.patch("os.path.exists", return_value=True),
        mock.patch("builtins.open", mock.mock_open(read_data='{"id": 1, "amount": 100')),
    ):
        result = read_transactions_json("data/operations.json")
        assert result == [], "Expected an empty list for invalid JSON"

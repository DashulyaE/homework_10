from src.transactions import read_transactions_csv, read_transactions_excel
from unittest import mock
import pandas as pd


def test_read_transactions_csv():
    mock_data = "id;state;date\n650703;EXECUTED;2023-09-05T11:30:32Z\n23598919;EXECUTED;2020-12-06T23:00:58Z\n"

    with mock.patch("builtins.open", mock.mock_open(read_data=mock_data)):
        result = read_transactions_csv("data/transactions.csv")
        expected_result = [
            {"id": "650703", "state": "EXECUTED", "date": "2023-09-05T11:30:32Z"},
            {"id": "23598919", "state": "EXECUTED", "date": "2020-12-06T23:00:58Z"},
        ]
        assert result == expected_result

    mock_empty_data = ""

    with mock.patch("builtins.open", mock.mock_open(read_data=mock_empty_data)):
        result = read_transactions_csv("data/transactions.csv")
        assert result == "Файл пустой или не верно заполнен"

    with mock.patch("builtins.open", side_effect=FileNotFoundError):
        result = read_transactions_csv("dummy_path.csv")
        assert result.startswith("Файл не найден, пустой или не верно заполнен. Ошибка:")


def test_read_transactions_excel():
    with mock.patch("pandas.read_excel") as mock_read_excel:
        # Создаем искусственные данные для возвращаемого DataFrame
        mock_df = pd.DataFrame(
            {
                "id": ["650703", "2023-01-02"],
                "state": ["EXECUTED", "EXECUTED"],
                "date": ["2023-09-05T11:30:32Z", "2020-12-06T23:00:58Z"],
            }
        )
        mock_read_excel.return_value = mock_df

        result = read_transactions_excel("data/transactions_excel.xlsx")

        expected_result = [
            {"id": "650703", "state": "EXECUTED", "date": "2023-09-05T11:30:32Z"},
            {"id": "2023-01-02", "state": "EXECUTED", "date": "2020-12-06T23:00:58Z"},
        ]
        assert result == expected_result

    with mock.patch("pandas.read_excel", side_effect=FileNotFoundError("File not found")):
        result = read_transactions_excel("data/transactions_excel.xlsx")
        assert result == "Файл не найден, пустой или не верно заполнен. Ошибка: File not found"

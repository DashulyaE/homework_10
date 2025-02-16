from src.processing import filter_by_state, sort_by_date
import pytest


@pytest.mark.parametrize(
    "state, result",
    [
        (
            "EXECUTED",
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            "CANCELED",
            [
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
        ),
        ("", []),
    ],
)
def test_filter_by_state(log_test: list[dict], state: str, result: list[dict]) -> None:
    assert filter_by_state(log_test, state) == result


@pytest.mark.parametrize(
    "sort_date, result",
    [
        (
            False,
            [
                {"id": 615064591, "state": "CANCELED", "date": "2015-10-14T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "2016-09-12T21:27:25.241689"},
                {"id": 939719570, "state": "EXECUTED", "date": "2017-06-30T02:08:58.425572"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 41428302, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
            ],
        ),
        (
            True,
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 41428302, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2017-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2016-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2015-10-14T08:21:33.419441"},
            ],
        ),
    ],
)
def test_sort_by_date(log_date: list[dict], sort_date: bool, result: list[dict]) -> None:
    assert sort_by_date(log_date, sort_date) == result

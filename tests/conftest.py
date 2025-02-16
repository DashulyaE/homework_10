import pytest


@pytest.fixture
def card_number() -> str:
    return "1596837868705199"


@pytest.fixture
def account_number() -> str:
    return "64686473678894779589"


@pytest.fixture
def log_test() -> list[dict]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def log_date() -> list[dict]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 41428302, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2017-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2016-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2015-10-14T08:21:33.419441"},
    ]

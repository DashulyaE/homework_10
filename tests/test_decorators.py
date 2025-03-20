from src.decorators import log
import pytest


def test_log(capsys):
    @log()
    def test_func(x, y):
        return x + y

    test_func(1, 3)
    captured = capsys.readouterr()
    assert "ok" in captured.out

    @log(filename="log.txt")
    def test_func2(a, b):
        return a * b

    test_func2(5, 4)

    with open("log.txt", "r") as file:
        log_content = file.read()
        assert "ok" in log_content

    @log()
    def test_func3(k, m):
        return k + m

    with pytest.raises(Exception):
        test_func3("2", 1)

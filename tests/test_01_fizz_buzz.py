import pytest
from solutions.task_01_fizz_buzz import fizz_buzz


def test_fizz_buzz(capfd):
    fizz_buzz()
    out, err = capfd.readouterr()
    results = out.strip().split('\n')
    assert len(results) == 100
    assert results.count('Fizz') == 27
    assert results.count('Buzz') == 14
    assert results.count('FizzBuzz') == 6
    assert err == ''  # no errors


if __name__ == '__main__':
    pytest.main([__file__])



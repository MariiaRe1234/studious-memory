import pytest
from solutions.task_56_ascii_numbers import get_name, FIRST_PERSON, SECOND_PERSON


@pytest.mark.parametrize("input_ascii, expected_output", [
    (FIRST_PERSON, "Mariia"),
    (SECOND_PERSON, "Oleksandr"),
    ([1001], '1001 nights with Scheherazade'),
    ([], ''),
    ([65, 66, 67], 'ABC'),
    (FIRST_PERSON + [1001], '1001 nights with Scheherazade'),
])
def test_get_name(input_ascii, expected_output):
    assert get_name(input_ascii) == expected_output


@pytest.mark.parametrize("invalid_input", [
    ([None]),
    (['a', 97]),
    123,
    None,
])
def test_get_name_invalid_input(invalid_input):
    with pytest.raises(TypeError):
        get_name(invalid_input)


if __name__ == '__main__':
    pytest.main([__file__])
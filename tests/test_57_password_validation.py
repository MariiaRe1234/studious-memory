import pytest
from solutions.task_57_password_validation import validate_password, string


@pytest.mark.parametrize("password, expected", [
    ("", False),  # empty
    ("short", False),  # too short < 8
    ("long" * 10, False),  # too long > 20
    ("abc12345!", False),  # missing uppercase
    ("ABCDEF@G", False),  # missing digit
    ("Abcdef12", False),  # missing punctuation
    ("Valid1!", True),
    ("Password#1", True),
    ("Invalid password1!", False),
    ("Pass!0"+string.punctuation, False),
    ("Abc@1234", True),  # 8 characters
    ("Qwertyu1!opASDfgh@1", True),  # 20 characters
    (12345678, False),  # integer
    ([123456, "abcde"], False),  # list
])
def test_validate_password(password, expected):
    assert validate_password(password) == expected


if __name__ == "__main__":
    pytest.main([__file__])
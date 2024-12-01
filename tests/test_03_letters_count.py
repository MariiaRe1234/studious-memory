import pytest
import string

from solutions.task_03_letters_count import count_letters, count_letters_algorithm_2

escape_list = string.whitespace + string.punctuation


@pytest.mark.parametrize("text,expected", [
    ("", None),
    ("    ", None),
    ("!!!", None),
    ("Hello World!!!", ('l', 3)),
    ("abcdefgABCDEFG", ('a', 2)),
    ("The quick brown fox jumps over the lazy dog.", ('o', 4)),
    ("Numbers123123133", ('1', 4)),
    ("CASEcaseCase", ('e', 3)),
    (escape_list, None)
])
def test_count_letters(text, expected):
    result = count_letters(text)
    assert result == expected


@pytest.mark.parametrize("text,expected", [
    ("", (None, 0)),
    ("    ", (None, 0)),
    ("!!!", (None, 0)),
    ("Hello World!!!", ('l', 3)),
    ("abcdefgABCDEFG", ('a', 2)),
    ("The quick brown fox jumps over the lazy dog.", ('o', 4)),
    ("Numbers123123133", ('1', 4)),
    ("CASEcaseCase", ('e', 3)),
    (escape_list, (None, 0))
])
def test_count_letters_algorithm_2(text, expected):
    result = count_letters_algorithm_2(text)
    assert result == expected


if __name__ == '__main__':
    pytest.main([__file__])
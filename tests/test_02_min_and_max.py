import pytest
from solutions.task_02_min_and_max import converted


@pytest.mark.parametrize('input_data, expected', [
    (['1', '2', '3'], [1, 2, 3]),                           # Normal string numbers
    (['one', 'two', '3'], [3]),                             # Mix of non-numeric and numeric strings
    ([1, 2, 3], [1, 2, 3]),                                 # Integer inputs
    ([1.1, 2.2, 3.3], [1, 2, 3]),                           # Floating point numbers
    ([None, '4', 'five'], [4]),                             # NoneType and strings
    (['6', '', '7'], [6, 7]),                               # Empty strings
    (['012', '003'], [12, 3]),                              # Strings with leading zeros
    ([], []),                                               # Empty list
    (['-1', '-2', '0'], [-1, -2, 0]),                       # Negative and zero values
    ([True, 1.5, '20'], [1, 1, 20]),                        # Boolean and mixed types
    (['0x11', '22', '0b11'], [0, 22, 0]),                   # Hexadecimal and binary interpreted string
    (['\t\n', '   ', '\n'], []),                            # Only whitespace strings
    ([float('inf'), '100', float('nan')], [100, 0]),        # Infinite and NaN floats
    (['1.9', '2.1'], [1, 2]),                               # Decimal strings are discarded due to int conversion
    ([object(), '123', complex(5)], [123]),                 # Object, string, and complex number
])
def test_converted(input_data, expected):
    result = converted(input_data)
    assert result == expected


def test_converted_ignores_invalid():
    input_data = ['abc', 'def', None, object(), True, 123]
    result = converted(input_data)
    assert all(isinstance(i, int) for i in result)


if __name__ == '__main__':
    pytest.main([__file__])
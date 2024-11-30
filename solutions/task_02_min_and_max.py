"""
There is a list:

numbers = [1, 2, '0', '300', -2.5, 'Dog', True, 0o1256, None]

Convert the elements of the list to type `int()`. Find the minimum and maximum value.

Ref: tasks/02_min_and_max.md
"""


items = [1, 2, '0', '300', -2.5, 'Dog', True, 0o1256, None]


def converted(numbers):
    res = []
    for i in numbers:
        try:
            res.append(int(i))
        except (ValueError, TypeError):
            continue
    return res


if __name__ == '__main__':
    integers = converted(numbers=items)
    print(f'min: {min(integers)}')
    print(f'max: {max(integers)}')
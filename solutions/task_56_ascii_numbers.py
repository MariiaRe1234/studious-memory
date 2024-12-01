"""
Write python function that converts numbers to text

Ref: tasks/56_ascii_numbers.md
"""

FIRST_PERSON = [77, 97, 114, 105, 105, 97]
SECOND_PERSON = [0x4f, 0x6c, 0x65, 0x6b, 0x73, 0x61, 0x6e, 0x64, 0x72]


def get_name(ascii_name):
    res = ''
    for i in ascii_name:
        if i == 1001:
            return '1001 nights with Scheherazade'
        res += chr(i)
    return res


if __name__ == '__main__':
    print(get_name(FIRST_PERSON))
    print(get_name(SECOND_PERSON))
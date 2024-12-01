"""
Implement function for validating user password. Password **must** match following criteria:
 - should be string
 - length between 8,20
 - must contain at least one capital letter
 - must contain at least one number
 - must contain at least one punctuation symbol
 - whitespace characters are not allowed

Function should return `boolean` value

Ref: tasks/57_password_validation.md
"""

import string


def validate_password(text):
    """
    :param text: User password
    :type text: str
    :rtype: bool
    """
    if not isinstance(text, str):
        return False
    if len(text) < 8 or len(text) > 20:
        return False
    if not any(i.isupper() for i in text):
        return False
    if not any(i.isdigit() for i in text):
        return False
    if not any(i in string.punctuation for i in text):
        return False
    if any(i.isspace() for i in text):
        return False
    return True


if __name__ == '__main__':
    print(validate_password('Hello'))
    print(validate_password('TerminatorT1000!'))
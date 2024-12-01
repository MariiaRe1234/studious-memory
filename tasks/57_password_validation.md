#### Password validation

Implement function for validating user password. Password **must** match following criteria:
 - should be string
 - length between 8,20
 - must contain at least one capital letter
 - must contain at least one number
 - must contain at least one punctuation symbol
 - whitespace characters are not allowed

Function should return `boolean` value

Notes:
 - use string.ascii_uppercase
 - use string.digits
 - use string.punctuation

```python
def validate_password(text):
    return False  # add your implementation
```

#### <u>Check yourself</u>:

```python
validate_password('Hello') == False
validate_password('TerminatorT1000!')
```
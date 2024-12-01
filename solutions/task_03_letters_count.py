"""
Determine which letter occurs most frequently in this text.

Answer the following questions:
 * How many times does the word 'Python' occur in this text?
 * How many times does your program read the text from beginning to end?
 * Will your solution work correctly if the text contains letters from the Ukrainian alphabet?

Ref: tasks/03_letters_count.md
"""

import string

text_from_wiki = """
Python is an interpreted high-level programming language for general-purpose programming. 
Created by Guido van Rossum and first released in 1991, Python has a design philosophy 
that emphasizes code readability, notably using significant whitespace. 
It provides constructs that enable clear programming on both small and large scales. 
In July 2018, the creator Guido Rossum stepped down as the leader in the language community after 30 years.
Python features a dynamic type system and automatic memory management. 
It supports multiple programming paradigms, including object-oriented, imperative, 
functional and procedural, and has a large and comprehensive standard library.
Python interpreters are available for many operating systems. CPython, the reference 
implementation of Python, is open source software and has a community-based development model, 
as do nearly all of Python's other implementations. Python and CPython are managed by the non-profit Python Software Foundation.
Вітання з Харкова!
"""

escape_list = string.whitespace + string.punctuation


def count_letters(text):
    text = text.lower()
    res = {}
    for i in text:
        if i in escape_list:
            continue
        if i in res:
            res[i] += 1
        else:
            res[i] = 1
    return sorted(res.items(), key=lambda pair: pair[1])[-1]


def count_letters_algorithm_2(text):
    text = text.lower()
    unique_text = set(i for i in text if i not in escape_list)
    l = None
    c = 0
    for i in unique_text:
        value = text.count(i)
        if value >= c:
            l = i
            c = value
    return l, c


if __name__ == '__main__':
    print(count_letters(text_from_wiki))
    print(count_letters_algorithm_2(text_from_wiki))
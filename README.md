# Python Tokenizer
A python project for tokenizing strings containing python code and identifying data types. This project can parse both Python data structures and arithmetic expressions.

---

## Features
- **Data Type Recognition**: Identifies all standard Python data types:
  - Text Types: `str`
  - Numeric Types: `int`, `float`, `complex`
  - Sequence Types: `list`, `tuple`, `range`
  - Mapping Types: `dict`
  - Set Types: `set`, `frozenset`
  - Boolean Types: `bool`
  - Binary Types: `bytes`, `bytearray`, `memoryview`
  - None Type: `NoneType`

-**Parsing Parameters** `strict` parameter for the `tokenize` function:
  - **Non-strict mode**: Preserves complex data structures and identifies their types.
  - **Strict mode**: Tokenizes arithemetic experessions character by character and can used to solve arithmetic statements.

-**Arithmetic**
  - This program can mathematically solve for the output of the tokenize function, which in turn allows the entire program to do arithmetic while taking in the entire mathematical statement as a string. This can be done with the `perform_arithmetic` function and is displayed within main.py

"""
Main file of the project which contains code for demonstration.
"""
from token_operations import (
    tokenize, perform_arithmetic
)

NON_STRICT_STR = """
[1, 2, 3] [4, 5, 6, 7] [8, 9, 10]
{'name': 'test', 'value': True} {'id': 123, 'act': False} {'items': ['a','b']}
('hi', 'bye') ('foo', 'bar', 42) ('hello', 'world')
42 100 999 1234
3.14 2.718 9.81 1.618
2+3j 4-2j 1+1j
{1, 2, 3} {4, 5, 6, 7} {8, 9}
frozenset({4, 5, 6}) frozenset({1, 2})
range(10) range(5, 15) range(0, 20, 2)
True False True
b'bytes' b'example' b'testing'
bytearray(b'bytearray') bytearray(b'example')
memoryview(b'memory') memoryview(b'test')
None None
'single quotes' "double quotes" 'more strings' "extra text"
+ + +
"""
STRICT_STR = "(5+10)*(20-15)/5"


def main():
    #  Demonstrate non-strict operations.
    non_strict_tokens = tokenize(NON_STRICT_STR, False)

    print("NON-STRICT TOKENIZE DEMO:")
    print(f"Input: {NON_STRICT_STR}")
    print(f"Output: {non_strict_tokens}\n")

    str_ct = 0
    int_ct = 0
    float_ct = 0
    complex_ct = 0
    list_ct = 0
    tuple_ct = 0
    range_ct = 0
    dict_ct = 0
    set_ct = 0
    frozenset_ct = 0
    bool_ct = 0
    bytes_ct = 0
    bytearray_ct = 0
    memoryview_ct = 0
    nonetype_ct = 0

    for token, token_type in non_strict_tokens:
        if token_type == "str":
            str_ct += 1
        elif token_type == "int":
            int_ct += 1
        elif token_type == "float":
            float_ct += 1
        elif token_type == "complex":
            complex_ct += 1
        elif token_type == "list":
            list_ct += 1
        elif token_type == "tuple":
            tuple_ct += 1
        elif token_type == "range":
            range_ct += 1
        elif token_type == "dict":
            dict_ct += 1
        elif token_type == "set":
            set_ct += 1
        elif token_type == "frozenset":
            frozenset_ct += 1
        elif token_type == "bool":
            bool_ct += 1
        elif token_type == "bytes":
            bytes_ct += 1
        elif token_type == "bytearray":
            bytearray_ct += 1
        elif token_type == "memoryview":
            memoryview_ct += 1
        elif token_type == "nonetype":
            nonetype_ct += 1

    print(f"{'Data Type':<25} {'Count':<25}")
    print("-" * 50)
    print(f"{'str':<25} {str_ct:<25}")
    print(f"{'int':<25} {int_ct:<25}")
    print(f"{'float':<25} {float_ct:<25}")
    print(f"{'complex':<25} {complex_ct:<25}")
    print(f"{'list':<25} {list_ct:<25}")
    print(f"{'tuple':<25} {tuple_ct:<25}")
    print(f"{'range':<25} {range_ct:<25}")
    print(f"{'dict':<25} {dict_ct:<25}")
    print(f"{'set':<25} {set_ct:<25}")
    print(f"{'frozenset':<25} {frozenset_ct:<25}")
    print(f"{'bool':<25} {bool_ct:<25}")
    print(f"{'bytes':<25} {bytes_ct:<25}")
    print(f"{'bytearray':<25} {bytearray_ct:<25}")
    print(f"{'memoryview':<25} {memoryview_ct:<25}")
    print(f"{'none':<25} {nonetype_ct:<25}")
    print()

    #  Demonstrate strict operations.
    strict_tokens = tokenize(STRICT_STR, True)
    math_solution = perform_arithmetic(strict_tokens)

    print("STRICT TOKENIZER DEMO:")
    print(f"Input: {STRICT_STR}")
    print(f"Output: {strict_tokens}")
    print(f"Mathematic Solution: {math_solution}")


if __name__ == "__main__":
    main()

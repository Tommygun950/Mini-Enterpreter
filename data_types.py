"""
All code pertaining to identifying individual data types.

Those data types include:
1. Text Types:
    a. str
2. Numeric Types:
    a. int
    b. float
    c. complex
3. Sequence Types:
    a. list
    b. tuple
    c. range
4. Mapping Types:
    a. dict
5. Set Types:
    a. set
    b. frozenset
6. Boolean Types:
    a. bool
7. Binary Types:
    a. bytes
    b. bytearray
    c. memoryview
8. None Type:
    a. NoneType
"""


def is_numeric_type(parsed_data: str) -> tuple[bool, str]:
    """
    Identifies if the data is of numeric type. If so,
    return the type of numeric data it is.
    """
    try:
        int(parsed_data)
        return (True, "int")

    except ValueError:
        try:
            float(parsed_data)
            return (True, "float")
        except ValueError:
            try:
                complex(parsed_data)
                return (True, "complex")
            except ValueError:
                return (False, "Non-numeric")


def is_sequence_type(parsed_data: str) -> tuple[bool, str]:
    """
    Identifies if the data is of sequence type. If so,
    return the type of sequence data it is.
    """
    if parsed_data.startswith("[") and parsed_data.endswith("]"):
        return (True, "list")
    elif parsed_data.startswith("(") and parsed_data.endswith(")"):
        return (True, "tuple")
    elif parsed_data.startswith("range(") and parsed_data.endswith(")"):
        return (True, "range")
    else:
        return (False, "non-sequence")


def is_mapping_type(parsed_data: str) -> tuple[bool, str]:
    """
    Identifies if the data is of mapping type. If so,
    return the type of mapping data it is.
    """
    if parsed_data.startswith("{") and parsed_data.endswith("}"):
        if len(parsed_data) > 2 and (":" in parsed_data):
            return (True, "dict")
        else:
            return (False, "non-mapping")
    else:
        return (False, "non-mapping")


def is_set_type(parsed_data: str) -> tuple[bool, str]:
    """
    Identifies if the data is of set type. If so,
    return the type of mapping data it is.
    """
    if parsed_data.startswith("{") and parsed_data.endswith("}"):
        if ":" not in parsed_data:
            return (True, "set")
    elif parsed_data.startswith("frozenset({") and parsed_data.endswith("})"):
        return (True, "frozenset")
    else:
        return (False, "non-set")


def is_boolean_type(parsed_data: str) -> tuple[bool, str]:
    """
    Identifies if the data is of boolean type. If so,
    return the type of mapping data it is.
    """
    if parsed_data == "True" or parsed_data == "False":
        return (True, "bool")
    else:
        return (False, "non-boolean")


def is_binary_type(parsed_data: str) -> tuple[bool, str]:
    """
    Identifies if the data is of binary type. If so,
    return the type of binary data it is.
    """
    frst_chars = parsed_data[:2]
    lst_char = parsed_data[-1]

    mem_view = parsed_data[11:]  # everything after "memoryview", for linting.

    if (frst_chars == "b'" or frst_chars == 'b"'):
        if (lst_char == "'" or lst_char == '"'):
            return (True, "bytes")
    elif parsed_data.startswith("bytearray(") and parsed_data.endswith(")"):
        return (True, "bytearray")
    elif parsed_data.startswith("memoryview(") and parsed_data.endswith(")"):
        if mem_view.startswith("b'") or mem_view.startswith('b"'):
            return (True, "memoryview")
    else:
        return (False, "non-binary")


def is_none_type(parsed_data: str) -> tuple[bool, str]:
    """
    Idenfies if the data is of none type. If so,
    return the type of none data it is.
    """
    if parsed_data == "None":
        return (True, "nonetype")
    else:
        return (False, "Non-nontype")

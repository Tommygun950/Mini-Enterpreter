"""
Contains all code for creating tokens and manipulating them.
Name: [Your Name Here]
"""

def tokenize(input: str) -> list[tuple[str, str]]:
    """
    Given a string containing arithmetic code,
    return the individual tokens with their types.
    Returns a list of tuples in the format (type, value).
    """
    parsed_data = parse_string(input)
    token_list = []
    for data in parsed_data:
        if data == "+":
            token_list.append(("PLUS", data))
        elif data == "-":
            token_list.append(("MINUS", data))
        elif data == "/":
            token_list.append(("DIVISION", data))
        elif data == "*":
            token_list.append(("MULTIPLICATION", data))
        elif data == "(":
            token_list.append(("LPAREN", data))
        elif data == ")":
            token_list.append(("RPAREN", data))
        elif data.isdigit():
            token_list.append(("NUM", data))
        else:
            raise ValueError(f"{data} is not a valid arithmetic character.")
    return token_list

def parse_string(input: str) -> list[str]:
    """
    Parse string into tokens while preserving multi-digit numbers.
    """
    tokens = []
    current_number = ""
    
    for char in input:
        if char.isdigit():
            current_number += char
        else:
            if current_number:
                tokens.append(current_number)
                current_number = ""
            
            if char in ['+', '-', '*', '/', '(', ')']:
                tokens.append(char)
    
    # Don't forget to add the last number if the string ends with a digit
    if current_number:
        tokens.append(current_number)
        
    return tokens

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
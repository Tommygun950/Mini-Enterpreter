from data_types import (
    is_numeric_type, is_sequence_type, is_mapping_type,
    is_set_type, is_boolean_type, is_binary_type,
    is_none_type
)


def tokenize(input: str, strict: bool = False) -> list[tuple[str, str]]:
    """
    Given a string containing arithmetic or python code,
    return the individual data types of each parsed section.

    strict = False -> will parse by data type.
    strict = True -> will parse every char and remove spacing.
    """
    parsed_data = parse_string(input, strict)

    token_list = []

    for data in parsed_data:
        is_numeric, numeric_type = is_numeric_type(data)

        if not strict:
            data_type = return_data_type(data)
            token = (data, data_type)
            token_list.append(token)
        elif strict:
            if data == "+":
                token = (data, "PLUS")
                token_list.append(token)
            elif data == "-":
                token = (data, "MINUS")
                token_list.append(token)
            elif data == "/":
                token = (data, "DIV")
                token_list.append(token)
            elif data == "*":
                token = (data, "MULTI")
                token_list.append(token)
            elif data == "(":
                token = (data, "LPAREN")
                token_list.append(token)
            elif data == ")":
                token = (data, "RPAREN")
                token_list.append(token)
            elif is_numeric and numeric_type == "int":
                token = (data, "NUM")
                token_list.append(token)
            else:
                raise ValueError(data, " not valid arithemetic char.")
    return token_list


def parse_string(input: str, strict: bool) -> list[str]:
    """
    Parse string into tokens while preserving complex data types.
    """
    if strict:
        return list(input.replace(" ", ""))
    elif not strict:
        tokens = []
        current_token = ""
        bracket_count = 0
        parenthesis_count = 0
        brace_count = 0

        for char in input:
            if char == "[":
                bracket_count += 1
            elif char == "]":
                bracket_count -= 1

            elif char == "(":
                parenthesis_count += 1
            elif char == ")":
                parenthesis_count -= 1

            elif char == "{":
                brace_count += 1
            elif char == "}":
                brace_count -= 1

            is_balanced = (bracket_count == 0 and
                           parenthesis_count == 0 and
                           brace_count == 0)

            if char.isspace() and is_balanced:
                if current_token:
                    tokens.append(current_token)
                    current_token = ""
            else:
                current_token += char

        if current_token:
            tokens.append(current_token)

        return tokens


def return_data_type(data: str) -> str:
    """
    Given the string, return the assumed data type.
    """

    is_numeric, numeric_type = is_numeric_type(data)
    if is_numeric:
        return numeric_type

    is_sequence, sequence_type = is_sequence_type(data)
    if is_sequence:
        return sequence_type

    is_mapping, mapping_type = is_mapping_type(data)
    if is_mapping:
        return mapping_type

    is_set, set_type = is_set_type(data)
    if is_set:
        return set_type

    is_boolean, boolean_type = is_boolean_type(data)
    if is_boolean:
        return boolean_type

    is_binary, binary_type = is_binary_type(data)
    if is_binary:
        return binary_type

    is_none, none_type = is_none_type(data)
    if is_none:
        return none_type

    return "str"


def perform_arithmetic(token_list: list[tuple[str, str]]) -> str:
    """
    If the individual tokens from the string are a functional arithmetic
    statement, return the calculated value as a string.
    """
    try:
        processed_tokens = []
        i = 0
        while i < len(token_list):
            token, token_type = token_list[i]

            if (token_type == "NUM" and i + 1 < len(token_list) and
               token_list[i + 1][1] == "NUM"):

                num_str = token
                j = i + 1
                while j < len(token_list) and token_list[j][1] == "NUM":
                    num_str += token_list[j][0]
                    j += 1

                processed_tokens.append((num_str, "NUM"))
                i = j
            else:
                processed_tokens.append((token, token_type))
                i += 1

        operand_stack = []
        operator_stack = []

        precedence = {  # for PEMDAS
            "PLUS": 1,
            "MINUS": 1,
            "MULTI": 2,
            "DIV": 2
        }

        for token, token_type in processed_tokens:
            if token_type == "NUM":
                operand_stack.append(int(token))

            elif token_type in ["PLUS", "MINUS", "MULTI", "DIV"]:
                while (operator_stack and
                       operator_stack[-1] != "LPAREN" and
                       precedence.get(operator_stack[-1], 0) >=
                       precedence.get(token_type, 0)):
                    apply_operation(operand_stack, operator_stack.pop())

                operator_stack.append(token_type)

            elif token_type == "LPAREN":
                operator_stack.append(token_type)

            elif token_type == "RPAREN":
                while operator_stack and operator_stack[-1] != "LPAREN":
                    apply_operation(operand_stack, operator_stack.pop())

                if operator_stack and operator_stack[-1] == "LPAREN":
                    operator_stack.pop()
                else:
                    raise ValueError("Mismatched parentheses")

        while operator_stack:
            op = operator_stack.pop()
            if op == "LPAREN":
                raise ValueError("Mismatched parentheses")
            apply_operation(operand_stack, op)

        if len(operand_stack) != 1:
            raise ValueError("Invalid arithmetic expression")

        return str(operand_stack[0])

    except Exception as e:
        return f"Unable to calculate: {str(e)}"


def apply_operation(operand_stack: list, operator: str) -> None:
    """
    Apply the given operation to the top two operands on the stack.
    """
    if len(operand_stack) < 2:
        raise ValueError("Not enough operands for operation")

    b = operand_stack.pop()
    a = operand_stack.pop()

    if operator == "PLUS":
        operand_stack.append(a + b)
    elif operator == "MINUS":
        operand_stack.append(a - b)
    elif operator == "MULTI":
        operand_stack.append(a * b)
    elif operator == "DIV":
        if b == 0:
            raise ValueError("Division by zero")
        operand_stack.append(a // b)

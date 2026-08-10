def tokenize(expression):
    expression = expression.replace(" ", "")
    if expression == "":
        raise ValueError("Expression cannot be empty")

    tokens = []
    i = 0

    while i < len(expression):
        char = expression[i]

        if char.isdigit() or char == ".":
            start = i
            dot_seen = False
            i += 1

            while i < len(expression) and (
                expression[i].isdigit() or (expression[i] == "." and not dot_seen)
            ):
                if expression[i] == ".":
                    dot_seen = True
                i += 1

            tokens.append(expression[start:i])
        elif char in "+-*/()":
            tokens.append(char)
            i += 1
        else:
            raise ValueError("Invalid characters in expression")

    return tokens

def evaluate_expression(expression):
    tokens = tokenize(expression)
    index = 0

    def parse_expression():
        nonlocal index
        value = parse_term()

        while index < len(tokens) and tokens[index] in ("+", "-"):
            operator = tokens[index]
            index += 1
            right = parse_term()

            if operator == "+":
                value += right
            else:
                value -= right

        return value
    
    def parse_term():
        nonlocal index
        value = parse_factor()

        while index < len(tokens) and tokens[index] in ("*", "/"):
            operator = tokens[index]
            index += 1
            right = parse_factor()

            if operator == "*":
                value *= right
            else:
                if right == 0:
                    raise ZeroDivisionError("Cannot divide by zero")
                value /= right

        return value
    
    def parse_factor():
        nonlocal index

        if index < len(tokens) and tokens[index] == "(":
            index += 1
            value = parse_expression()

            if index >= len(tokens) or tokens[index] != ")":
                raise ValueError("Mismatched parentheses")

            index += 1
            return value

        if index < len(tokens) and tokens[index] in ("+", "-"):
            operator = tokens[index]
            index += 1
            value = parse_factor()

            if operator == "-":
                return -value
            return value

        if index >= len(tokens):
            raise ValueError("Invalid expression")

        token = tokens[index]
        index += 1

        try:
            return float(token)
        except ValueError as exc:
            raise ValueError("Invalid expression") from exc

    result = parse_expression()

    if index != len(tokens):
        raise ValueError("Invalid expression")

    return result

if __name__ == "__main__":
    print("Simple Calculator")

    while True:
        try:
            expression = input("Enter expression (or 'quit' to exit): ")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break

        if expression.strip().lower() in {"quit", "exit"}:
            print("Goodbye!")
            break

        try:
            result = evaluate_expression(expression)
            if result.is_integer():
                print(int(result))
            else:
                print(result)
        except Exception as exc:
            print(f"Error: {exc}")

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



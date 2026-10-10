from abobakr_tools import read_float, read_integer


def perform_binary_operation(operation: str) -> None:
    """تنفيذ العمليات الحسابية الثنائية (+, -, *, /, %, //)."""
    first_operand = read_float("Enter the first number: ")
    second_operand = read_float("Enter the second number: ")

    if operation in ["/", "%", "//"]:
        while second_operand == 0:
            print("The program cannot perform this operation when the second number is 0.")
            exit_command = input(
                "If you want to stop the program, type 'stop'. Otherwise, press Enter: "
            )

            if exit_command.lower().strip() == "stop":
                return

            second_operand = read_float("Enter the second number: ")

    if operation == "+":
        result = first_operand + second_operand
    elif operation == "-":
        result = first_operand - second_operand
    elif operation == "*":
        result = first_operand * second_operand
    elif operation == "/":
        result = first_operand / second_operand
    elif operation == "%":
        result = first_operand % second_operand
    elif operation == "//":
        result = first_operand // second_operand
    else:
        return
    print(f"Result: {result}")


def perform_power_operation() -> None:
    """تنفيذ عملية الأسس (^)."""
    base_number = read_integer("Enter the number: ")
    exponent = read_integer("Enter the exponent: ")

    while base_number == 0 and exponent < 0:
        print("The program cannot calculate 0 raised to a negative exponent.")

        exit_command = input(
            "If you want to stop the program, type 'stop'. Otherwise, press Enter: "
        )

        if exit_command.lower().strip() == "stop":
            return

        base_number = read_integer("Enter the number: ")
        exponent = read_integer("Enter the exponent: ")

    result = base_number ** exponent
    print(f"Result: {result}")


def perform_root_operation() -> None:
    """تنفيذ عملية الجذور (sqrt)."""
    radicand = read_float("Enter the number: ")

    while radicand < 0:
        print("The number under the root cannot be less than 0.")

        exit_command = input(
            "If you want to stop the program, type 'stop'. Otherwise, press Enter: "
        )

        if exit_command.lower().strip() == "stop":
            return

        radicand = read_float("Enter the number: ")

    root_degree = read_float("Enter the root degree: ")

    while root_degree <= 0:
        print("The root degree must be greater than 0.")

        exit_command = input(
            "If you want to stop the program, type 'stop'. Otherwise, press Enter: "
        )

        if exit_command.lower().strip() == "stop":
            return

        root_degree = read_float("Enter the root degree: ")

    result = radicand ** (1 / root_degree)
    print(f"Result: {result}")


def main() -> None:
    operation_guide = [
        "+     : Addition",
        "-     : Subtraction",
        "*     : Multiplication",
        "/     : Division (may return a decimal number)",
        "//    : Floor division",
        "%     : Modulo (remainder)",
        "^     : Exponentiation (example: 2^3 = 8)",
        "sqrt  : Root (example: sqrt 25 = 5)",
    ]

    for description in operation_guide:
        print(description)

    while True:
        selected_operation = input(
            "Enter an operation (+, -, *, /, ^, %, //, sqrt) or 'stop' to exit: "
        ).strip()

        if selected_operation in ["+", "-", "*", "/", "%", "//"]:
            perform_binary_operation(selected_operation)
        elif selected_operation == "sqrt":
            perform_root_operation()
        elif selected_operation == "^":
            perform_power_operation()
        elif selected_operation == "stop":
            return
        else:
            continue

if __name__ == "__main__":
    main()

import collections

variables = {}


def check_element(element):
    return -1 if element.count("-") % 2 else 1


def parse_command(user_input):
    if user_input[1:] == "exit":
        print("Bye!")
        exit()
    elif user_input[1:] == "help":
        print("The program calculates addition and subtraction")
    else:
        print("Unknown command")


def parse_assignment(user_input):
    left, right = map(lambda x: x.strip(), user_input.split("=", 1))
    # c = 7 -  1 = 5 too many values to unpack if the arg is not given
    if left.isalpha():
        if right.isnumeric() or right in variables:
            if right.isnumeric():
                variables[left] = int(right)
            else:
                variables[left] = variables[right]
        else:
            print("Invalid assignment")
    else:
        print("Invalid identifier")


def infix_to_postfix(user_input):
    digits = []
    digit = ""
    for char in user_input:
        if char.isnumeric():
            digit += char
        elif char in variables:
            digits.append(variables[char])
            digit = ""
        else:
            digits.append(int(digit))
            digit = ""
    print(digits)


def postfix_to_result(postfix):
    pass


def parse_expression(user_input):
    infix_to_postfix(user_input)
    # postfix_to_result(postfix)


while True:
    user_input = "".join(input().split())
    if user_input == "":
        pass

    elif user_input.startswith("/"):
        parse_command(user_input)

    elif "=" in user_input:
        parse_assignment(user_input)

    else:
        parse_expression(user_input)

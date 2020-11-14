# http://www.cs.nthu.edu.tw/~wkhon/ds/ds10/tutorial/tutorial2.pdf
# https://youtu.be/vXPL6UavUeA
# https://youtu.be/QCnANUfgC-w

import string
import collections


def parse_command(user_input):

    if user_input[1:] == "exit":
        print("Bye!")
        exit()
    elif user_input[1:] == "help":
        print("""This calculator evaluates expressions with addition, subtraction,
multiplication, division, power, unary operators and parenthesis.
It can also assign and use variables. Variable names can contain only
Latin letters. Type \"/exit\" to quit.""")

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


def parse_expression(infix):

    postfix_list = infix_to_postfix(infix)
    if postfix_list == "Error":
        return "Invalid expression"
    result = postfix_to_result(postfix_list)
    return result


def infix_to_postfix(infix):

    result = []
    stack = collections.deque()
    i = 0

    while i < len(infix):

        # Check for integer or variable
        if i < len(infix) and (infix[i] in string.digits or infix[i] in string.ascii_letters):

            # Find end of integer and append it to result, reset sign to positive
            if infix[i] in string.digits:
                integer = 0
                while i < len(infix) and infix[i] in string.digits:
                    integer = integer * 10 + int(infix[i])
                    i += 1
                result.append(integer)

            # Find end of variable name and append it to result
            else:
                var_name = ""
                while i < len(infix) and infix[i] in string.ascii_letters:
                    var_name += infix[i]
                    i += 1
                result.append(var_name)

        # Check for unacceptable symbols
        elif i < len(infix) and infix[i] not in "+-*/^()":
            return "Error"

        # Check for operator or parentheses
        if i < len(infix) and infix[i] in "+-*/^()":

            # Push left parenthesis onto stack
            if infix[i] == "(":
                stack.append("(")
                i += 1

            # Resolve addition operator, ignore multiple pluses
            elif infix[i] == "+":
                while stack and stack[-1] in "+-*/^":
                    result.append(stack.pop())
                stack.append("+")
                while i < len(infix) and infix[i] == "+":
                    i += 1

            # Resolve subtraction operator, depending on number of minuses
            elif infix[i] == "-":
                while stack and stack[-1] in "+-*/^":
                    result.append(stack.pop())
                minuses = 0
                while i < len(infix) and infix[i] == "-":
                    minuses += 1
                    i += 1
                if minuses % 2:
                    stack.append("-")
                else:
                    stack.append("+")
            # Resolve multiplication or division operator
            elif infix[i] in "*/":
                if i < len(infix) - 1 and infix[i + 1] == infix[i]:
                    return "Error"
                while stack and stack[-1] in "*/^":
                    result.append(stack.pop())
                stack.append(infix[i])
                i += 1

            # Resolve power operator
            elif infix[i] == "^":
                if i < len(infix) - 1 and infix[i + 1] == infix[i]:
                    return "Error"
                while stack and stack[-1] == "^":
                    result.append(stack.pop())
                stack.append(infix[i])
                i += 1

            # Resolve right parenthesis
            elif infix[i] == ")":
                while stack and stack[-1] != "(":
                    result.append(stack.pop())
                if not stack:
                    return "Error"
                else:
                    stack.pop()
                    i += 1

    # Append all remaining operators from stack to result
    while stack:
        if stack[-1] == "(":
            return "Error"
        result.append(stack.pop())

    return result


def postfix_to_result(postfix_list):

    stack = collections.deque()
    for i in range(len(postfix_list)):
        if isinstance(postfix_list[i], int):
            stack.append(postfix_list[i])

        elif postfix_list[i] in "+-*/^":
            if len(stack) < 2:
                return "Invalid expression"
            if postfix_list[i] == "+":
                stack.append(stack.pop() + stack.pop())
            elif postfix_list[i] == "*":
                stack.append(stack.pop() * stack.pop())
            elif postfix_list[i] == "^":
                power = stack.pop()
                stack.append(stack.pop() ** power)
            elif postfix_list[i] == "-":
                subtrahend = stack.pop()
                stack.append(stack.pop() - subtrahend)
            elif postfix_list[i] == "/":
                divisor = stack.pop()
                if divisor == 0:
                    return "Invalid expression"
                stack.append(stack.pop() // divisor)
        else:
            try:
                stack.append(variables[postfix_list[i]])
            except KeyError:
                return "Unknown variable"
    if len(stack) > 1:
        return "Invalid expression"
    if not len(stack):
        return ""
    return stack.pop()


variables = {}  # dictionary to hold variables
while True:
    # remove all whitespace from expression
    user_input = "".join(input().split())
    if user_input:
        if user_input.startswith("/"):
            parse_command(user_input)
        elif "=" in user_input:
            parse_assignment(user_input)
        else:
            result = parse_expression(user_input)
            print(result, end="\n")

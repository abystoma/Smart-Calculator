def check_element(element):
    return -1 if element.count("-") % 2 else 1


variables = {}

while True:
    user_input = input()
    if user_input == "":
        pass

    elif user_input.startswith("/"):
        if user_input[1:] == "exit":
            print("Bye!")
            break
        elif user_input[1:] == "help":
            print("The program calculates addition and subtraction")
        else:
            print("Unknown command")

    elif "=" in user_input:
        left, right = map(lambda x: x.strip(), user_input.split("=", 1))
        #c = 7 -  1 = 5 too many values to unpack if the arg is not given
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
    else:
        elements = user_input.split()
        if len(elements) == 1:
            if elements[0].isnumeric():
                print(int(elements[0]))
            elif elements[0] in variables:
                print(variables[elements[0]])
            else:
                print("Unknown variable")
        else:

            try:
                if elements[0].isnumeric():
                    sum = int(elements[0])
                else:
                    sum = variables[(elements[0])]
                for i in range(1, len(elements), 2):
                    if elements[i + 1].isnumeric():
                        sum += check_element(elements[i]) *int(elements[i + 1])
                    else:
                        sum += check_element(elements[i]) * variables[(elements[i + 1])]
                        

                print(sum) 
            except IndexError:
                print("Invalid expression")
            except KeyError:
                print("Unknown variable")

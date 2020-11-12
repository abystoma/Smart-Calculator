def check_element(element):
    try:
        return int(element)
    except ValueError:
        return "-1" if element.count("-") % 2 else "1"


while True:
    user_input = input()

    if user_input == '/exit':
        print('Bye!')
        break
    elif user_input == "/help":
        print("The program calculates the sum of numbers")
    elif user_input == '':
        continue
    else:
        elements = user_input.split()
        try:
            sum = int(elements[0])
            sign = "1"
            for element in range(1, len(elements)):
                check = check_element(element)
                if type(check) == int:
                    sum += int(sign) * check
                else:
                    sign = check
            print(sum)
        except Exception:
            print("Invalid expression")

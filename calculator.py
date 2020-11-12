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
        print(sum(map(int, user_input.split())))

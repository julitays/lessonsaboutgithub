# This is my first project for GitHub, I'm going to do my calculator!

print('Hello, how are you? I want to show you my new calculator. Are you going to try it?')

digit_1, digit_2 = map(int, input('Введите два числа: ').split())

while True:
    operation = input('Введите операцию, "stop" или "x" для выхода: ')
    if operation == '+':
        print(digit_1 + digit_2)

    elif operation == '-':
        print(digit_1 - digit_2)

    elif operation == '*':
        print(digit_1 * digit_2)

    elif operation == '/':
        if digit_1 == 0 or digit_2 == 0:
            print('На ноль делить нельзя, как и ноль, собственно, на что-то тоже!')
        else:
            print(digit_1 / digit_2)
    elif operation == '%':
        print(digit_1 % digit_2)
    # Остаток от деления
    elif operation == '//':
        if digit_1 == 0 or digit_2 == 0:
            print('На ноль делить нельзя, как и ноль, собственно, на что-то тоже!')
        else:
            print(digit_1 // digit_2)
    # Целочисленное деление
    elif operation == '**':
        print(digit_1 ** digit_2)
    elif operation == 'stop' or operation == 'x' or operation == 'X':
        break
    else:
        print('Введите операцию!')
        continue




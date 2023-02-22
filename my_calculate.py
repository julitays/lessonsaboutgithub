# This is my first project for GitHub, I'm going to do my calculator!

print('Hello, how are you? I want to show you my new calculator. Are you going to try it?')

x, y = map(int, input('Введите два числа: ').split())


while True:
    oper = input('Введите операцию, 'stop' или 'x' для выхода: ')
    if oper == '+':
        print(x + y)

    elif oper == '-':
        print(x - y)

    elif oper == '*':
        print(x * y)

    elif oper == '/':
        if x == 0 or y == 0:
            print('На ноль делить нельзя, как и ноль, собственно, на что-то тоже!')
        else:
            print(x / y)
    elif oper == '%':
        print(x % y)
    # Остаток от деления
    elif oper == '//'':
        if x == 0 or y == 0:
            print('На ноль делить нельзя, как и ноль, собственно, на что-то тоже!')
        else:
            print(x // y)
    # Целочисленное деление
    elif oper == '**':
        print(x ** y)
    elif oper == 'stop' or 'x':
        break
    else:
        print('Введите операцию!')
        continue




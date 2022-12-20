# This is my first project for GitHub, I'm going to do my calculator!

x, y = int(input('Введите число 1: ')), int(input('Введите число 2: '))


while True:
    oper = input('Введите операцию: ')
    if oper == '+':
        print(x+y)

    elif oper == '-':
        print(x-y)

    elif oper == '*':
        print(x*y)

    elif oper == '/':
        if x == 0 or y == 0:
            print('На ноль делить нельзя, как и ноль, собственно, на что-то тоже!')
        else:
            print(x / y)

    elif oper == '%':
        print(x%y)

    elif oper == '//':
        if x == 0 or y == 0:
            print('На ноль делить нельзя, как и ноль, собственно, на что-то тоже!')
        else:
            print(x // y)

    elif oper == '**':
        print(x**y)

    elif oper == 'stop':
        break
    else:
        print('Введите правильную операцию!')
        continue




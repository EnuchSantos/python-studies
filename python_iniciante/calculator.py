leave = False
result = 0

while not leave:

    number_1 = input('Type a number: ')
    operator = input('Type a operator (+ - * /): ')
    number_2 = input('Type another number: ')

    try:
        number_1 = float(number_1)
        number_2 = float(number_2)
    except:
        print('You not type a number!')

    operator_check = True
    if operator == '+':
        result = number_1 + number_2
    elif operator == '-':
        result = number_1 - number_2
    elif operator == '*':
        result = number_1 * number_2
    elif operator == '/':
        result = number_1 / number_2
    else:
        print('The operator is invalid!')
        operator_check = False

    if operator_check is True:
        print(f'Result: {number_1} {operator} {number_2} {result}')

    leave = input('Desire left? [Y]es: ').lower().startswith('y')

    if leave is True:
        break

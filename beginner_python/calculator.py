leave = False
result = 0

while not leave:

    number_1 = input('Type a number: ')
    operator = input('Type a operator (+-*/): ')
    number_2 = input('Type another number: ')

    try:
        number_1 = float(number_1)
        number_2 = float(number_2)
    except:
        print('You not type a number!')
        continue

    if operator not in '+-/*':
        print('The operator is invalid!')
        continue

    if len(operator) > 1:
        print('The more than an operator was typed')
        continue

    if operator == '+':
        result = number_1 + number_2
    elif operator == '-':
        result = number_1 - number_2
    elif operator == '*':
        result = number_1 * number_2
    elif operator == '/':
        result = number_1 / number_2
    else:
        print('Aaaaaaaaaaaauuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu')

    print(f'Result: {number_1} {operator} {number_2} {result}')

    leave = input('Desire left? [Y]es: ').lower().startswith('y')

    if leave is True:
        break

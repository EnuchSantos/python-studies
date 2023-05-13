"""
Ask to user to type a int number and tell the user if is even or odd,
if number is not a int, tell the user that is not a int number
"""

int_number = input('Type an int number: ')

try:
    int_number = int(int_number)

    if int_number % 2 == 0:
        print("It's an even number!")
    else:
        print("It's an odd number!")
except:
    print('The number is not an int')

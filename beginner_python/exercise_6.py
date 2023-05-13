"""
Ask to user what time is it
"""

time = input('Tell the time: ')

try:
    time = int(time)
    if 0 <= time <= 11:
        print('Good morning')
    elif 11 < time <= 17:
        print('Good afternoon')
    elif 17 < time <= 23:
        print('Good night')
    else:
        print('the time doesnt exists')
except:
    print("You don't type a number")

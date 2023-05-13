first_name = input('Type your first name: ')

if len(first_name) <= 4:
    print("Short name")
elif 5 <= len(first_name) <= 6:
    print("Normal name")
else:
    print('Big name')

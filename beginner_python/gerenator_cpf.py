import random

nine_digits = ''
for i in range(9):
    nine_digits += str(random.randint(0, 9))

first_digit = 0
count = 0
for i in range(10, 1, -1):
    first_digit += int(nine_digits[count]) * i
    count += 1

first_digit = (first_digit * 10) % 11
first_digit = 0 if first_digit > 9 else first_digit

ten_digits = nine_digits + str(first_digit)
second_digit = 0
count = 0
for i in range(11, 1, -1):
    second_digit += int(ten_digits[count]) * i
    count += 1

second_digit = (second_digit * 10) % 11
second_digit = 0 if second_digit > 9 else second_digit
cpf = ten_digits + str(second_digit)
print(cpf)

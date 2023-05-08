import re

cpf = re.sub(r'[^0-9]', '', '70166845477')  # apenas nums de 0-9

CPF = '70166845477' \
    .replace('.', '') \
    .replace('-', '') \
    .replace(' ', '')

count = 0
sum = 0
for i in range(10, 1, -1):
    sum += int(CPF[count]) * i
    count += 1

result_1 = (sum * 10) % 11

first_digit = 0 if result_1 > 9 else result_1

count = 0
sum = 0
for i in range(11, 1, -1):
    sum += int(CPF[count]) * i
    count += 1

result_2 = (sum * 10) % 11

second_digit = 0 if result_2 > 9 else result_2

cpf_do_usuario = f'{CPF[:9]}{first_digit}{second_digit}'
if cpf_do_usuario == CPF:
    print('CPF válido!')
else:
    print('CPF inválido!')

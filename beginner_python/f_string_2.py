"""
> - Esquerda
< - Direita
^ - Centro
Sinal - + ou _
Ex.: 0>-100,.1f
Conversion flags - !r !s !a
"""

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.')
print(f'{100.000:.1f}')
print(f'{100.000:0=+10,.1f}')
print(f'O hexadecimal de 1500 é {1500:08x}')
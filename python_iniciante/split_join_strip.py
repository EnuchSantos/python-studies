"""
Split e Join com list e str
Split - divide uma string
Join - Une uma string
"""

phrase = '  Olhá só que, coisa interessante  '
word_list = phrase.split(',')

word_list_formated = []
for i, frase in enumerate(word_list):
    # lstrip left e rstrip right
    word_list_formated.append(word_list[i].strip())

# print(word_list_formated)
phrases_uni = ', '.join(word_list_formated)
print(phrases_uni)

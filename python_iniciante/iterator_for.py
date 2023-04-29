"""
Iterável -> str. range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o proximo valor
iter -> me entregue seu iterador
"""

text = iter("Enuch")  # __iter__()

print(text.__next__())
print(text.__next__())
print(text.__next__())
print(text.__next__())
print(next(text))

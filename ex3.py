'''
3. Având 2 liste, [3, 1, 0, 2] și [6, 5, 4]
Găsește 2 variante să le unești într-o singură listă.
'''

a = [3, 1, 0, 2]
b = [6, 5, 4]
c = [6, 5, 4]
print(a+b)
b.extend(a)
print(b)
print([*a, *c]) # unpaching
print(sum([a,c], []))
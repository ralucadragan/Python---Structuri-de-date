'''
1.
Set
zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
● Adaugă în zilele_sapt ‘luni’
● Afișează zile_sapt
'''
zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
zile_sapt.add('luni')
print(zile_sapt)
print('----------------------------------------------------------------')
'''
2.Folosește un if și verifică dacă:
● Weekend este un subset al zilelor din săptămânii.
● Weekend nu este un subset al zilelor din săptămânii.
'''
if weekend.issubset(zile_sapt):
    print('Weekend este un subset al zilelor  săptămânii.')
else:
    print('Weekend nu este un subset al zilelor  săptămânii.')
print('----------------------------------------------------------------')

# 3. Afișează diferențele dintre aceste 2 seturi.
print(zile_sapt - weekend)
print('----------------------------------------------------------------')

# 4. Afișează intersecția elementelor din aceste 2 seturi
print(zile_sapt & weekend)

'''
11. Gigel se transferă din clasă
● Căuta o funcție care să îl șteargă
● Vine un coleg nou. Adaugă Ionică, cu nota 9
● Printează noii elevi
'''

dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
dict1.pop('Gigel')
print(f'Dupa plecarea colegului in clasa raman urmatorii elevi: {dict1}')

dict1['Ionica'] = 9
print(f'Dupa sosirea noului coleg, in clasa vor fi urmatorii elevi: {dict1}')
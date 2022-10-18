'''
1. Declară o listă note_muzicale în care să pui do re mi etc până la do
● Afișeaz-o.
● Inversează ordinea folosind slicing și suprascrie această listă.
● Printează varianta actuală (inversată).
● Pe această listă aplică o metodă care bănuiești că face același lucru,
adică să îi inverseze ordinea. Nu trebuie să o suprascrii în acest caz,
deoarece metoda face asta automat.
● Printează varianta actuală a listei. Practic ai ajuns înapoi la varianta
inițială.
Concluzii: slicing e temporar, dacă vrei să păstrezi nouă variantă va trebui să
suprascrii lista sau să o salvezi într-o listă nouă. Metoda găsită de tine face
suprascrierea automat și permanentizează aceste modificări. Ambele variante
își găsesc utilitatea în funcție de ce ne dorim în acel moment.
'''
from typing import List

note_muzicale = ['do', 're', 'mi', 'fa', 'sol','la', 'si', 'do']
print(f'Notele muzicale sunt :', note_muzicale)
note_muzicale_invers = note_muzicale [::-1]
print(f'Notele muzicale inversate sunt :', note_muzicale_invers)
# print(f'Notele muzicale inversate sunt :',note_muzicale[::-1])

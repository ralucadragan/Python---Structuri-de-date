'''
1. Ne imaginăm o echipă de fotbal pt teren sintetic.
3 Schimbări maxime admise:
● Declară o Listă cu 5 jucători
● Schimbari_efectuate = te joci tu cu valori diferite
● Schimbari_max = 3
Dacă Jucătorul x e în teren și mai avem schimbări la dispoziție
- Efectuează schimbarea
- Șterge jucătorul scos din listă
- Adaugă jucătorul intrat
- Afișază a intrat x, a ieșit y, mai ai z schimbări
Dacă jucătorul nu e în teren:
- Afișază ‘nu se poate efectua schimbarea deoarece jucătorul x nu e în
teren’
- Afișază ‘mai ai z schimbări’
Testează codul cu diferite valori
'''

jucatori_teren = ['Marian', 'Dorel', 'Ovidiu', 'Catalin', 'Ion']
schimbari_efectuate = 2
schimbari_max = 3
jucator_cautat = "Gigel"

if schimbari_max - schimbari_efectuate > 0:

        if jucator_cautat in jucatori_teren:
            print(f'Ok, jucatorul {jucator_cautat} este pe teren.')
            jucatori_teren.remove('Dorel')
            jucatori_teren.append('Mircea')
            print(f'A intrat jucatorul: {jucatori_teren[4]} si a iesit jucatorul: {jucator_cautat}, mai ai {schimbari_max-schimbari_efectuate} schimbari.')
        else :
            print(f'Nu se poate efectua schimbarea deoarece jucatorul {jucator_cautat} nu este in teren.')
            print(f'Mai ai {schimbari_max - schimbari_efectuate} schimbari.')
else:
    print('Nu se mai pot efectua schimbari.')
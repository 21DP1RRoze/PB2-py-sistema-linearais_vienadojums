'''
Programma pārbauda lietotāja zināšanas par matemātikas tēmu "Lineārs vienādojums"
Tiek parādīta teorija, doti uzdevumi un pārbaudes darbs.

Izveidoja: Roberts Rozenvalds DP1-1
'''

from operator import ne
import os # 
import time

def teorijas_lasisana(): # 1. daļa - teorijas daļa.
    faila_mainigais = open('teorija.txt', 'r', encoding='utf-8') # Atver failu ar pareizo šifrēšanu.
    rinda = faila_mainigais.readline()
    print("> > > Lūdzu izlasi teoriju par šo tēmu! ") 
    while rinda != '': # kamēr nav EOF
        print(rinda, end='') # Izprintē katru rindu 1 pēc otras un turpina, tikai ja lietotājs nospiedis "enter" taustiņu.
        rinda= faila_mainigais.readline()
        input("> > > Nospiediet \"Enter\", lai turpinātu! ")
        os.system('cls')
    print("> > > Teorijas beigas! Malacis!")
    faila_mainigais.close()

teorijas_lasisana() # 1. daļas izsaukšana

turpinajums = False
while turpinajums == False: # vai lietotājs vēlas izlasīt teoriju vēlreiz? Ja jā, tiek izsaukta funkcija teorijas_lasisana, ja nē, programma turpinās
    atbilde = input("Vai vēlaties teoriju lasīt velreiz? (ja/ne) ")
    atbilde = atbilde.replace(" ", "")
    if atbilde.lower() == "ja":
        os.system('cls')
        teorijas_lasisana()
    elif atbilde.lower() == "ne":
        turpinajums = True
        os.system('cls')
    else:
        print("Nepareiza komanda. Lūdzu, ievadiet \"ja\" vai \"ne\". ")

def uzdevumu_pildisana(): # 2. daļa - trenēšanās uzdevumi.
    fails_uzdevumi = open('uzdevumi.txt', 'r', encoding='utf-8') # Atver failu ar pareizo šifrēšanu.
    fails_atbildes = open('atbildes.txt', 'r', encoding='utf-8') # Atver failu ar pareizo šifrēšanu.
    rindaUzd = fails_uzdevumi.readline().replace("\n","").replace("$ ", "\n") # Failā "$ " norāda nākamo rindu, lai skaistāk izskatītos.
    rindaAtb = fails_atbildes.readline().replace("\n","")
    print("> > > Lūdzu izpildi šos uzdevumus!")
    print()
    while rindaUzd != '': # kamēr nav EOF
        print(rindaUzd, end='') # Izprintē katru rindu 1 pēc otras un turpina tikai ja lietotājs ievadījis atbildi.
        atbilde = input().replace(" ", "").replace(",", ".")
        if atbilde.lower() == rindaAtb: # Ja atbilde sakrīt ar to, kas norādīta failā, programma attiecīgi paziņo.
            print("Pareizi! Atbilde ir {0}.".format(rindaAtb))
            print()
            time.sleep(1)
        else: # Ja atbilde nesakrīt
            print("Diemžēl nepareizi. Pareizā atbilde ir {0}.".format(rindaAtb))
            print()
            time.sleep(1)
        rindaUzd= fails_uzdevumi.readline().replace("\n","").replace("$ ", "\n") # Programma izlasa nākamo rindu failā.
        rindaAtb = fails_atbildes.readline().replace("\n","")
    fails_uzdevumi.close()
    fails_atbildes.close()
        
uzdevumu_pildisana() # 2. daļas izsaukšana

turpinajums = False # vai lietotājs vēlas izpildīt uzdevumus  vēlreiz? Ja jā, tiek izsaukta funkcija uzdevumu_pildisana, ja nē, programma turpinās
while turpinajums == False:
    atbilde = input("Vai vēlaties uzdevumus pildīt velreiz? (ja/ne) ")
    atbilde = atbilde.replace(" ", "")
    if atbilde.lower() == "ja":
        os.system('cls')
        uzdevumu_pildisana()
    elif atbilde.lower() == "ne":
        turpinajums = True
        os.system('cls')
    else:
        print("Nepareiza komanda. Lūdzu, ievadiet \"ja\" vai \"ne\". ")

def pd_pildisana(): # 3. daļa - pārbaudes darbs.
    fails_uzdevumi = open('pd.txt', 'r', encoding='utf-8') # Atver failu ar pareizo šifrēšanu.
    fails_atbildes = open('atbildesPD.txt', 'r', encoding='utf-8') # Atver failu ar pareizo šifrēšanu.
    rindaUzd = fails_uzdevumi.readline().replace("\n","").replace("$ ", "\n")
    rindaAtb = fails_atbildes.readline().replace("\n","")
    print("> > > Pārbaudes darbs par Jūsu zināšanām! 10 jautājumi")
    print()
    punkti = 0
    while rindaUzd != '': # kamēr nav EOF
        print(rindaUzd, end='') # Izprintē katru rindu 1 pēc otras un turpina, tikai ja lietotājs ievadījis atbildi.
        atbilde = input().replace(" ", "").replace(",", ".")
        if atbilde.lower() == rindaAtb: # Ja lietotāja ievadītā atbilde sakrīt ar failā norādīto, tiek pieskaitīts punkts.
            punkti += 1
            print()
            time.sleep(1)
        else: # Ja atbilde nesakrīt
            print()
            time.sleep(1)
        rindaUzd= fails_uzdevumi.readline().replace("\n","").replace("$ ", "\n")
        rindaAtb = fails_atbildes.readline().replace("\n","")
    time.sleep(2)
    os.system('cls')
    print("Jūs pabeidzāt pārbaudes darbu ar rezultātu {0}/10! Procentuāli tie ir {1}%".format(punkti, punkti/10*100)) # rezultāti tiek parādīti punktos un procentuāli
    fails_uzdevumi.close()
    fails_atbildes.close()

pd_pildisana() # 3. daļas izsaukšana.

os.system('pause')
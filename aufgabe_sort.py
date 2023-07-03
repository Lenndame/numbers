"""
einfach

Gib zwei Zahlen a und b aufwärts sortiert aus.
Verwende einfache Datentypen wie int. Keine Listen, sort() oder ähnliches.


Prüfe den Algorithmus mit folgenden Zahlen
a = 9, b = 8
a = 9, b = 10

Beispiel
a = 3
b = 2

Antwort:
2, 3
"""
#a = 9
#b = 10

"""
mittel

Bestimme die Größte aus drei vorher festgelegten Zahlen und gib diese Zahl aus. Verwende einfache Datentypen wie int. Keine Listen, sort()
oder ähnliches.

Prüfe mit folgenden Zahlen:
a = 2, b = 343, c = 1
a = 12, b = 3, c = 2
a = 4, b= 11, c = 24

Beispiel
a = 33, b = 2, c = 23
Antwort:
Die größte Zahl ist a mit dem Wert 33
"""
#a = 4
#b = 11
#c = 24

#-------------------------------------------------------------------
# Teil 1.
#-------------------------------------------------------------------

userinputa1 = int(input("Hier Zahl a angeben: "))
userinputb1 = int(input("Hier Zahl b angeben: "))

if userinputa1 > userinputb1:
    print(userinputa1,",", userinputb1)
elif userinputb1 > userinputa1:
    print(userinputb1,",", userinputa1)
else:
    print("UserError: Entweder invalide Eingabe oder die Zahlen sind gleich groß. Prüfe deine Eingabe!")

#-------------------------------------------------------------------
# Teil 2.
#-------------------------------------------------------------------

userinputa2 = int(input("Hier Zahl a angeben: "))
userinputb2 = int(input("Hier Zahl b angeben: "))
userinputc2 = int(input("Hier Zahl c angeben: "))

if userinputa2 > userinputb2 and userinputa2 > userinputc2:
    print("A ist die größte Zahl mit dem Wert:", userinputa2 )
elif userinputb2 > userinputa2 and userinputb2 > userinputc2:
    print("B ist die größte Zahl mit dem Wert:", userinputb2 )
elif userinputc2 > userinputa2 and userinputc2 > userinputb2:
    print("C ist die größte Zahl mit dem Wert:", userinputb2 )
else:
    print("Alles gleich groß? oder eine andere falsche Eingabe? ")

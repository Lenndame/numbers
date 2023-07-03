"""
Berechne den Body-Mass-Index:

Der Body-Mass-Index (kurz: BMI) ist eine Zahl, mit der man abschätzen kann, 
ob man Unter-, Normal oder Übergewicht hat. Man berechnet diese Zahl nach der folgenden Formel:

          Gewicht
BMI = ---------------
       Größe * Größe

Dabei wird das Gewicht in kg und die Größe in m angegeben.
Runde auf zwei Nachkommastellen.

über Input wird das Gewicht in Gramm (g) eingegeben und die Höhe in cm. Rechne
die Eingabewerte entsprechend um und berechne das Ergebnis. Lege dafür passende
Variablen an.
"""

height = int(input("Größe in cm: ")) / 10000
weight = int(input("Gewicht in g: ")) / 10000

bmi = weight / (height * height)
print("Der BMI beträgt: ", round(bmi, 2))
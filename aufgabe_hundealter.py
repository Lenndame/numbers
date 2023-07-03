"""
Allgemein rechnet man Hundejahre in Menschenjahre um, indem man das Alter des Hundes mit 7 multipliziert. Je nach
Hundegröße und Rasse sieht die Umrechnung jedoch etwas komplizierter aus, z.B.:

- Ein einjähriger Hund entspricht in etwa einem 14-jährigen Menschen.
- 2 Jahre eines Hundes entsprechen 22 Jahre eines Menschen.
- Ab wann entspricht ein Hundejahr jeweils 5 Menschenjahren.

Schreibe ein Programm, das das Alter eines Hundes erfragt und dann nach obiger Methode berechnet, welchem Alter in Menschenjahren das entspricht.
Beachte, dass ein Hund mindestens 1 Jahr alt sein muss!

Ein Hund mit drei Jahren ist also 22 + ((3 - 2) * 5) Jahre alt.
"""

human_age = float(input("wie alt ist der Hund? "))

if human_age == 1:
    dog = 14
    print("Der Hund ist", dog, "Jahre in Hundejahren alt.")
elif human_age == 2:
    dog = 22
    print("Der Hund ist", dog, "Jahre in Hundejahren alt.")
elif human_age > 2:
    dog = 22 + ((human_age - 2) * 5)
    print("Der Hund ist", dog, "Jahre in Hundejahren alt.")

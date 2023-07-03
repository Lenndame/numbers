import random


# random library bietet Funktionen zum Erstellen von Zufallszahlen
# # https://docs.python.org/3/library/random.html

# zufallszahl zwischen 1 und 8. Dazu nutzen wir randint(1,8)
random_number = random.randint(1, 8)

# einfach
# Aufgabe: in welchen Wertebereich fällt die Zahl. Schreibe dazu die
# nötigen Bedingungen und printe das Ergebnis aus.

# a) 6-8
# b) 3-5
# c) 1-2

# Beispiel-Lösung: die gewürfelte Zahl ist im Wertebereich a zuhause

print(random_number)
if random_number >= 6 and random_number <= 8:
    print("Bereich a) 6-8")
elif random_number >= 3:
    print("Bereich b) 3-5")
else:
    print("Bereich c) 1-2")
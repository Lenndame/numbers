"""
Aufgaben zum Thema Zahlen und Listen. 
Erstelle die nötigen Varialben und printe das Ergebnis aus.
Du kannst für jede Aufgabe eine eigene Datei erstellen.
"""

"""
Rechne Meter in cm um.
40 Meter. Wieviele Cm?

meters = 40
"""


"""
Gib die Datentypen folgender Variablen mit der print-Funktion aus:

a = 0.5
b = 2
c = 4_000
d = None
e = 'omicron Tagesstern'
f = [2, 3]
g = {}
"""
#Teilaufgabe 1

meter = int(input("wie viele Meter sollen umgerechnet werden? "))
centimeter = meter * 100
print("...calculating...")
print("Thank you for choosing python to do simple math")
print( meter,"m sind", centimeter, "cm")
print(" ")

#Teilaufgabe 2
 
print("a ist ", type(0.5))
print("b ist ", type(2))
print("c ist ", type(4_000))
print("d ist ", type(None))
print("e ist ", type('omicron Tagesstern'))
print("f ist ", type([2, 3]))
print("g ist ", type({}))

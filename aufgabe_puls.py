"""
Aufgabe:
 Der optimale Puls bei Ausdauersportarten hängt vom Alter ab. Er lässt sich 
 mit der Formel Puls = 165 - 0.75 * Alter bestimmen. 

So ist der optimale Puls für 18 Jahre 151
Schreibe ein Programm, das folgenden Dialog ermöglicht:

Alter: über input einzugeben
Ausgabe: optimaler Puls
"""

age = int(input("Wie alt sind sie? "))

beat = 165 - 0.75 * age

print("Ihr optimalerPuls liegt bei: ", int(beat))

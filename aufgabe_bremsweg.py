"""
Anhalteweg:

Es gibt folgende Faustformeln zur Berechnung von Anhaltewegen:

Reaktionsweg (in Metern) = (Geschwindigkeit (in km/h) geteilt durch 10) mal 3

Bremsweg (in Metern) = (Geschwindigkeit (in km/h) geteilt durch 10) mal (Geschwindigkeit (in km/h) geteilt durch 10)

Anhalteweg (in Metern) = Reaktionsweg plus Bremsweg

Eingabe: km/h (via input-funktion)

Gebe den Reaktionsweg, den Bremsweg und den Anhalteweg 
entsprechend der km/h aus. Hinweis: 124.4 ist ein gültiger Eingabewert.
"""

speed = float(input("Die Geschwindigkeit in km/h beträgt: ")) 

speed10 = speed / 10
reactiontime = speed10 * 3 
breaktime = speed10 **2 
distance = reactiontime + breaktime

print("Der Anhalteweg beträgt: ", round(distance), "m")
print("Der Bremsweg beträgt: ", round(breaktime), "m")
print("Der Reaktionsweg beträgt: ", round(reactiontime), "m")

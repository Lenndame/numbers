"""
Rechne die angegebnen Minuten in Tage, Stunden und Minuten um
nutze dazu floordiv und modulo

MINUTES_DAY = 24 * 60 

Wieviele Tage sind 3434 Minuten?
Wieviele Stunden und Minuten bleiben dann noch übrig?

Beispiel

minuten = 3434 

sind 2 Tage, 9 Stunden und 14 Minuten

"""
total_mins = int(input("Wie viele Minuten möchtest du umrechnen? "))

MINUTES_WEEK = 60 * 24 * 7
MINUTES_DAY = 60 * 24

weeks = total_mins // MINUTES_WEEK
daysrest = total_mins % MINUTES_WEEK
days = daysrest // MINUTES_DAY
rest = total_mins % MINUTES_DAY
hours = rest // 60
minutes = rest % 60

print("Es sind: ", weeks, "Wochen",  round(days), "Tage", round(hours), "Stunden und ", round(minutes), "Minuten")

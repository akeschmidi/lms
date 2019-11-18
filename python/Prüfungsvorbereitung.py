#definietion von i mit dem Wert 42
i = 42

#definition von A mit einem String
Hallo = "Dies ist ein Hallo"


#Wahr oder Falsch
ichHabeDenWertWahr = True
ichHabeDenWertFalsch = False
print("HALLO")


#Operationen 

#Division
10 / 3
#Addition
10 + 3
#Subtraktion
10 - 1
#Multiplikation
10 * 2


#Array wird definiert
cars = ["Ford", "Volvo", "Tesla","BMW", "Honda", "Ferrai", "Trabi"]

#Ausgabe aller im Array enthaltenen Werte
print(cars)


#Erster Wert im Array 
print(cars[2])

#Mehrer Werte ausgeben
print(cars[5])
print(cars[6])


#Übungsaufgabe while Funktion:
i = 0
while i <= 100:
  print(i)
  i += 1

#Ifelse
a = 33
b = 200
if b > a:
  print("Gebe etwas aus")


#Elif 
a = 33
b = 33
if b > a:
  print("b ist groesser als a")
elif a == b:
  print("a und b ist gleich")



##Simple Funktion
def my_function():
  print("Hello from a function")
  print("Hallo von der zweiten Reihe")
  x=1
  print(x)
my_function()



##Zusammen hängende funktionen 
def my_function(vorname):
  print(vorname + " Mueller")
  
my_function("Emil")
my_function("Tobias")
my_function("Linus")
my_function("Max")


##Mehre Werte aus/mitgeben
def my_function(land = "Schweiz"):
  print("Ich bin von: " + land)
my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

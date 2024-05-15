# Opgave 1:
# Schrijf een functie die de tafel van “factor” afdrukt (zie ook opgave 5 uit het hoofdstuk Besturingsstructuren).
# Bijvoorbeeld als factor = 5:

# 1 x 5 = 5
# 2 x 5 = 10
# 3 x 5 = 15    # enz.

# De header van de functie is:
def print_tafel(factor):
    for i in range(1, 11):
        print(i, 'x', factor, '=', i * factor)

print_tafel(5)


# Opmerking: Maak een testset om de functie te testen. Gebruik het hoofdprogramma om die test uit te voeren.

# Opgave 2:
# Schrijf een functie die bepaalt of 2 getallen een veelvoud van elkaar zijn.
# De functie geeft True of False terug. Ga ervan uit die de twee getallen positief en geheel zijn.


# De header van de functie is:

def is_veelvoud(a, b):
    # Schrijf een eenvoudig hoofdprogramma om je functie in te gebruiken.
    if a % b == 0 or b % a == 0:
        return True
    else:
        return False


print(is_veelvoud(4, 2))





# Opgave 3:
# Schrijf een functie die een “productregel” afdrukt.


# 2 x 5 = 10 is de productregel bij 2 en 5
# 6 x 8 = 48 is de productregel bij 6 en 8


# De header van de functie is:
def print_productregel(aantal, tafel) :
    print(aantal, 'x', tafel, '=', aantal * tafel)

print_productregel(2, 5)
print_productregel(6, 8)

def print_tafel2(factor):
    for i in range(1, 11):
        print_productregel(i, factor)



# Schrijf een eenvoudig hoofdprogramma om je functie in te gebruiken.

# aannames: aantal ≥ 0 en 0 ≤ tafel ≤ 10

# Pas vervolgens de body van de functie print_tafel() uit opgave 1 aan.
# Maak in deze body gebruik van de functie print_productregel().

# Test vervolgens de nieuwe versie van print_tafel met hetzelfde testprogramma dat je bij opgave 1 gebruikt hebt.
# In het geval van een blackbox test kun je dus ook dezelfde testset gebruiken.

print_tafel2(5)

# Opgave 4
# Schrijf een functie die Celsius naar Fahrenheit converteert, met de volgende header:

def cels_to_fahr (celsius) :
    fahrenheit = (9 / 5) * celsius + 32
    return fahrenheit.__round__(2)

print(cels_to_fahr(40))
print(cels_to_fahr(32))


# N.B. De formule voor de conversie is als volgt: fahrenheit = (9 / 5) * celsius + 32
# Schrijf een programma dat een for-statement gebruikt en hierbij de functie cels_to_fahr() aanroept om de volgende uitvoer te produceren:
# Celsius            Fahrenheit

# 40.00              104.00
# 39.00              102.20
# 38.00              100.40
# 37.00              98.60
# 36.00              96.80
# 35.00              95.00
# 34.00              93.20
# 33.00              91.40
# 32.00              89.60
# 31.00              87.80
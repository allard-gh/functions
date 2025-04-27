# ==========================================
# Voorbeeld Opdracht
# Schrijf een functie die de tekst “Hello, World!” print. Roep vervolgens de functie aan.
# ==========================================
import random


def print_hello_world():
    print('Hello, World!')

print_hello_world()  # Uitkomst: Hello, World!

# ==========================================
# Opdracht 1:
# Print de tafel van 5 met behulp van een for-loop en een functie (genaamd 'print_tafel_regel').
# De factor en for-loop zijn al gegeven. Schrijf de functie om de regel van de tafel te printen.
#
# Verwachte uitkomst:
# 1  x  5  =  5
# 2  x  5  =  10
# 3  x  5  =  15 enz.
# ==========================================

factor = 5

def tafel_van_vijf(aantal):
    print(f'{aantal} x {factor} = {aantal * factor}')

for i in range(1, 11):
    tafel_van_vijf(i)

#proberen met gebruikersinput
# tafel = int(input('Van welk getal wil je de tafel weten? '))
# level = int(input('Tot welke trap wil je de tafel? '))
# print(f'De tafel van {tafel} tot trap {level}: ')
#
# def tot_waar(trap):
#     print(f'{trap} * {tafel} = {trap * tafel}')
#
# for l in range(1, level + 1):
#     tot_waar(l)

# ==========================================
# Opdracht 2:
# Maak een dobbelsteen met de volgende deelopdrachten.
#
# Opdracht 2a:
# Maak met behulp van de bibliotheek (library) 'random' een functie die een willekeurig getal tussen 1 en 6 genereert.
# Zorg dat de functie twee argumenten ontvangt, namelijk 'min' en 'max'. Voor het minimum (1) en maximum (6).
# Voer de functie 10 keer uit (met een for-loop). Als het willekeurige getal is gegenereerd print je het getal.
#
# Opdracht 2b;
# Maak een variabele aan 'aantal_keer_zes' en zet deze op 0. Schrijf een functie die aan het eind print hoe vaak er een 6 is gegooid.
# De variabele 'aantal_keer_zes' moet in de print statement worden gebruikt.
#
# Verwachte uitkomst (voorbeeld):
# 3 7 2 6 1 4 5 6 2 1
# Er is 2 keer een 6 gegooid
# ==========================================

aantal_keer_zes = 0

import random
def dobbel(minimum, maximum):
    """willekeurig getal tussen meegegeven min en max"""
    return random.randint(minimum, maximum)

for i in range(10):
    worp = dobbel(1, 6)
    print(worp, end=' ')

print()

def dobbel_twee(aantal):
    """dobbelsteen waarbij aantal keer 6 geteld wordt. Aantal worpen moet meegegeven worden"""
    global aantal_keer_zes
    aantal_keer_zes = 0
    for worp in range(aantal):
        getal = random.randint(1, 6)
        print(getal, end=' ')
        if getal == 6:
            aantal_keer_zes += 1
    print(f'\nAantal keer 6 gegooid: {aantal_keer_zes}')

dobbel_twee(10)

# ==========================================
# Opdracht 3:
# Omrekenen van Fahrenheit naar Celsius. Gegeven zijn temperaturen van drie steden in Fahrenheit.
#
# Schrijf een functie die de temperatuur in Fahrenheit ontvangt als argument en deze omrekent naar Celsius.
# De formule voor de conversie is als volgt: celsius = (fahrenheit - 32) * 5/9
# Schrijf ook een functie die de temperatuur afrondt in hele getallen.
# print de temperatuur in Celsius afgerond op hele getallen.
#
# Verwachte uitkomst:
# 18
# 24
# 40
# ==========================================

temp_in_fahr_stockholm = 65
temp_in_fahr_sydney = 75
temp_in_fahr_cairo = 104

def f_to_c(fahrenheit):
    """omrekenen fahrenheit naar celsius"""
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def afronden(getal):
    """afronden op heel getal"""
    afgerond = round(getal)
    return afgerond

print(afronden(f_to_c(temp_in_fahr_stockholm)))
print(afronden(f_to_c(temp_in_fahr_sydney)))
print(afronden(f_to_c(temp_in_fahr_cairo)))

# van de uitwerkingen (global wordt hier niet gebruikt)
# def genereer_willekeurig_getal(min, max):
#     return random.randrange(min, max)
#
#
# def controleer_op_zes(willekeurig_getal):
#     if willekeurig_getal == 6:
#         return True
#     else:
#         return False
#
#
# for worp in range(10):
#     willekeurig_getal = genereer_willekeurig_getal(1, 7)
#     print(willekeurig_getal, end=' ')
#     if controleer_op_zes(willekeurig_getal):
#         aantal_keer_zes += 1
#
# print('\nEr is', aantal_keer_zes, 'keer een 6 gegooid')
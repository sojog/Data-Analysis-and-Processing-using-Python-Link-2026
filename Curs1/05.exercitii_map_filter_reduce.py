# Creați o funcție Python care primește o listă de întregi ca argument și returnează o nouă listă care conține doar șirurile mai lungi decât 5 caractere
# lista = [10, 2, 30, 50, 300, 10]


def siruri_mai_lungi_de_5(lista):
    return list(filter(lambda x: len(str(x)) > 5, lista ))

print(siruri_mai_lungi_de_5([10, 2, 30, 50, 300_000, 10]))

## Definiți o funcție Python care primește un string ca argument și returnează un nou string în care toate vocalele au fost eliminate
# vocale = "aeiouAEIOU"
# input_string = "Salutare, ce mai faci?"
from functools import reduce

def fara_vocale(text):
    return reduce(lambda x, y: x+y, filter(lambda x: x not in "aeiouAEIOU", text))

print(fara_vocale("Salutare, ce mai faci?"))

## Scrieți o funcție Python care primește o listă de numere ca argument și returnează media acestora
# fără a folosi funcțiile sum/len.

lista = [10, 30, 20, 100]

def media(lista):
    return reduce(lambda x, y: x + y, lista) / reduce(lambda x, y: x + 1, lista, 0)

print(media(lista))




              
                   
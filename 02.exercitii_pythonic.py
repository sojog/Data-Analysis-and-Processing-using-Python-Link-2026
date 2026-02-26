# Creați o funcție Python care primește o listă de întregi ca argument și returnează o nouă listă care conține doar șirurile mai lungi decât 5 caractere
# lista = [10, 2, 30, 50, 300, 10]

## LIST COMPREHENTION

def siruri_mai_lungi_de_5(lista):
    return [i for i in lista  if len(str(i)) > 5]
  

print(siruri_mai_lungi_de_5([10, 2, 30, 50, 300_000, 10]))

## Definiți o funcție Python care primește un string ca argument și returnează un nou string în care toate vocalele au fost eliminate
# vocale = "aeiouAEIOU"
# input_string = "Salutare, ce mai faci?"

## LIST COMPREHENTION

def fara_vocale(text):
    vocale = "aeiouAEIOU"
    return "".join( [  ch  for ch in text if ch not in vocale ]   )
    

print(fara_vocale("Salutare, ce mai faci?"))

## Scrieți o funcție Python care primește o listă de numere ca argument și returnează media acestora
# fără a folosi funcțiile sum/len.

lista = [10, 30, 20]

def media(lista):
    suma = 0
    lungimea = 0
    for i in lista:
        lungimea += 1
        suma += i    
    return suma / lungimea if lungimea else 0

print(media(lista))
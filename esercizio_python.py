print("Test per ambiente phyton")

def somma(operando1, operando2):
    print("Faccio la somma")
    return operando1 + operando2

    def differenza(minuendo, sottraendo):
        return minuendo - sottraendo

def moltiplicazione(moltiplicando, moltiplicatore):
    return moltiplicando * moltiplicatore


def divisione(dividendo, divisore):
    risultato = dividendo / divisore
    return risultato

print("1. Somma")
print("2. Differenza")
print("3. Moltiplicazione")
print("4. Divisione")

scelta = int(input())

print("Inserisci il primo valore")
valore1 = int(input())
print("Inserisci il secondo valore")
valore2 = int(inpu())

risultato = 0
if scelta == 1:
    risultato = somma("valore1, valore2")
elif scelta == 2:
    risultato = sottrazione("valore1, valore2")
elif scelta == 3:
    risultato = moltiplicazione("valore1, valore2")
elif scelta == 4:
    risultato = divisione("valore1, valore2")
else:
    print("Operazione non riconosciuta")


print(risultato)


    




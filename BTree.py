from math import floor, ceil

print("DATI:")
try: 
    NR = int(input("Inserire il numero di record...........(NR): "))
    assert NR > 0, "NR deve essere maggiore di 0"

    R = int(input("Inserire la dimensione di ogni record...(R): "))
    assert R > 0, "R deve essere maggiore di 0"

    K = int(input("Inserire la dimensione della chiave.....(K): "))
    assert K > 0, "K deve essere maggiore di 0"

    CB = int(input("Inserire la dimensione di ogni blocco..(CB): "))
    assert CB > 0, "CB deve essere maggiore di 0"

    P = int(input("Inserire la dimensione dei puntatori....(P): "))
    assert P > 0, "P deve essere maggiore di 0"

    mode = int(input("I blocchi devono essere riempiti per intero(0) o a meta'(1)? (0/1): "))
    assert mode == 0 or mode == 1, "Inserire 0 o 1."
except ValueError:
    print("Inserire solamente numeri!")
    exit()

# calcolo del numero di record che entrano in un blocco
M = 0
if mode == 1: M = ceil((CB/2) / R)
else:         M = CB // R

# calcolo del numero di blocchi per il file principale
BF = ceil(NR / M)

# dimensione di in record indice
RI = K + P

# Massimo numero di record indice che entrano in un blocco
if mode == 1: MI = ceil(((CB / 2) - P) / RI) + 1
else:         MI = ((CB - P) // RI) + 1

# calcolo del numero di livelli necessari per il file indice
levels = [ceil(BF / MI)]
if levels[0] != 1:
    currLevel = 1
    while True:
        BN = ceil(levels[currLevel-1] / MI)
        levels.append(BN)
        if BN == 1:
            break
        currLevel += 1

# numero di accessi per la ricerca
NA = len(levels) + 1

res = ("\nRISULTATI:\n"
      f"Massimo numero di record per blocco del file principale:....{M}\n"
      f"Numero di blocchi necessari per il file principale:.........{BF}\n"
      f"Massimo numero di record indice per blocco de file indice:..{MI}")
print(res)

BTOT = BF
for i, lvl in enumerate(levels):
    print(f"Numero di blocchi per livello indice {i+1}:.....................{lvl}")
    BTOT += lvl

print(f"Numero di accessi necessari per la ricerca:.................{NA}")
print(f"Numero totale di blocchi per tutta la struttura:............{BTOT}")
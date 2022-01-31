from math import floor, ceil

print("DATI:")
try:
    NR = int(input("Inserire il numero di record...........(NR): "))
    assert NR > 0, "NR deve essere maggiore di 0"

    R = int(input("Inserire la dimensione di ogni record...(R): "))
    assert R > 0, "R deve essere maggiore di 0"

    CB = int(input("Inserire la dimensione di ogni blocco..(CB): "))
    assert CB > 0, "CB deve essere maggiore di 0"

    P = int(input("Inserire la dimensione dei puntatori....(P): "))
    assert P > 0, "P deve essere maggiore di 0"

    B = int(input("Inserire il numero di bucket............(B): "))
    assert B > 0, "B deve essere maggiore di 0"
except ValueError:
    print("Inserire solamente numeri!")
    exit()

# Record che entrano in un bucket
RB = ceil(NR / B)

# Massimo numero di record che entrano in un blocco del file principale
M = (CB - P) // R

# Blocchi necessari per ogni bucket
BB = ceil(RB / M)

# Puntatori che entrano in un blocco
PB = CB // P

# Numero di blocchi necessari per la bucket directory
BD = ceil(B / PB)

# Numero totale di blocchi per la struttura hash
BTOT = BD + BB * B

# Numero di accessi per la ricerca
NA = ceil(BB / 2)

res = ("\nRISULTATI:\n"
      f"Numero di record per bucket:........................{RB}\n"
      f"Massimo numero di record che entrano in un blocco:..{M}\n"
      f"Numero di blocchi necessari per ogni bucket:........{BB}\n"
      f"Numero di puntatori che entrano in un blocco:.......{PB}\n"
      f"Numero di blocchi per la bucket directory:..........{BD}\n"
      f"Numero di blocchi totali per la struttura hash:.....{BTOT}\n"
      f"Numero di accessi per la ricerca:...................{NA}")

print(res)
from math import log, ceil, floor

print("DATI:")
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

print("\nPERCENTUALE UTILIZZO BLOCCHI:")
POF = int(input("Percentuale riempimento blocchi del file principale (inserici senza il simbolo di percentuale %): "))
assert POF > 0 and POF <= 100, "Attenzione, la percentuale di riempimento dei blocchi del file principale deve essere compresa tra 1 e 100"
if POF < 100: answPOF = int(input(f"I blocchi del FILE PRINCIPALE devono essere riempiti al piu'(0) o almeno(1) al {POF}%? (0/1): "))

POI = int(input("Percentuale riempimento blocchi del file indice (inserici senza il simbolo di percentuale %): "))
assert POI > 0 and POI <= 100, "Attenzione, la percentuale di riempimento dei blocchi del file indice deve essere compresa tra 1 e 100"
if POI < 100: answPOI = int(input(f"I blocchi DEL FILE INDICE devono essere riempiti al piu'(0) o almeno(1) al {POI}%? (0/1): "))


# dimensione di un record indice
RI = P + K

# Massimo numero di record per blocco del file principale
M = 0
if(POF == 100): M = CB // R
else:           M = ceil(CB * (POF / 100)) / R

if(POF < 100): 
    if answPOF == 1: M = ceil(M)
    else:            M = floor(M)
else: M = floor(M)

# Numero di blocchi per file principale
assert M != 0, "Attenzione, M (massimo numero di record che entrano in un blocco del file principale) risulta essere = 0"
BF = ceil(NR / M)

# Massimo numero di record indice per blocco
MI = 0
if(POI == 100): MI = CB // RI
else:           MI = ceil(CB * (POI / 100)) / RI

if(POI < 100): 
    if answPOI == 1: MI = ceil(MI)
    else:            MI = floor(MI)
else: MI = floor(MI)

# Numero di blocchi per file indice
BI = ceil(BF / MI)

# Calcolo del numero di accessi
ACC = ceil(log(BI, 2)) + 1

res = ("\nRISULTATI:\n"
       f"Massimo numero di record per blocco del file principale:.....{M}\n"
       f"Numero di blocchi necessari per il file principale:..........{BF}\n"
       f"Massimo numero di record indice per blocco del file indice:..{MI}\n"
       f"Numero di blocchi necessari per il file indice:..............{BI}\n"
       f"Numero di accessi necessari:.................................{ACC}")

print(res)
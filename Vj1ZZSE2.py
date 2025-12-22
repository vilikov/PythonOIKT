# Omogućiti korisniku unos jednog broja,
# a zatim ispisati da li je broj paran ili neparan,
# te da li je broj pozitivan ili negativan


broj = (int)(input('Unesite broj: '))

print("Uneseni broj je")

if broj % 2 == 0:
    print("  - paran")
else:
    print("  - neparan")

if broj > 0:
    print("  - pozitivan")
elif broj < 0:
    print("  - negativan")
else:
    print("  - nula")

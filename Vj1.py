broj = 7 / 3
print(7 // 3)
print(7 / 3)  # odma pretvara u float

# pythona nije briga za promjenu varijabli niti tipova
broj = "neki string"
print(broj)

# provjera tipa
print(1, 2, 3, "\n", broj, " je ", type(broj))

# mnozenje stringom ovo je inace zabranjeno ne mozemo staviti + ili slicno ovo jedino finckionira
a = "neki text" * 3
print(a)

# dakle ovo ne a = 'neki text' + 3 medjutim mozemo:

# ako pretvorimo u str on ce zapravo pretvoriti 3 u '3'
broj = 3
a = "neki tekst " + str(broj)
print(a)

# tekst u broj
print(type(float("0")))

# uzimanje od korisnika
a = input("Upisite nesto: ") # uzima cijelu liniju do entera
print("upisali ste: ", a, " sto god upisali to je uvijek ", type(a))

#deklaracija varijabli 
a, b, c, = 1, True, 3.3

b = None # nema niceg
b = 10 == 10 and 10 != 15 or not 2>3 # and i or se navode rijecima a ne && i ||

print(b)


# nemamo zagrade, dvotovka otvara blok a blok uvlacimo 
if a < 3:
    print('manji od 3')

# string je neizmjenjiv 
a = 'neki tekst' #ovo je odma polje
print('index 2 ', a[2], len(a))

# mozemo i ici odostraga
print('index polja -3 ', a[-3])

# string range

print(a[0:4]) # od 0 do 3 


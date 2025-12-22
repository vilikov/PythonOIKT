

# Vili Kovac

rijec = input('Unesite rijec: ')

if '0' <= rijec[0] <= '9':
    print(rijec[1:])
else:
    print('OK')


# pretpostavljam da se radi provjeri samo jedne znamenke jer petlje nisu obuhvacene prvom vjezbom
# ako rijec pocinje viseznamenkastim brojem
# i = 0
# while i < len(rijec) and '0' <= rijec[i] <= '9':
#   i = i +1
#print(rijec[i:])

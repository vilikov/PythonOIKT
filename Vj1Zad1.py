# je li broj troznamenkast 

broj = int(input('Upisi mi neki broj: '))

if broj >= 0 and broj < 10:
    print('jednoznamenkast')
elif broj < 100:
    print('dvoznamenkast')
elif broj < 1000:
    print('troznamenkast')
else:
    print('izvan raspona')



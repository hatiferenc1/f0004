név = input('Hogy hívnak? ')
kor = input('És hány éves vagy? ')
kor = int(kor) 
év = input('Melyik évet írunk? ')
év = int(év)
születési_év = év - kor
print(név, ', kend ', születési_év, '-ban született.', sep='')

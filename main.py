hai = 'hi '
myname = input('ketikkan nama = ')  # str, int => int(input('ketikkan nomor = '))
mynumb = len(myname)
apakah = True
choose = ['yes', 'no']

if mynumb >= 10:
    apakah = True
    print(choose[0].upper())
else:
    apakah = False
    print(choose[1].upper())

while mynumb <= 5:
    print(mynumb)
    mynumb = mynumb + 1

ell = hai + myname.upper() + ' ' + str(mynumb) + ' ' + str(apakah)

print(ell, '... terdapat', myname.count('a'), 'huruf a pada nama')

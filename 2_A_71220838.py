nama = input('masukkan nama: ')
z = len(nama)
for i in range(z):
    for x in range(i+1):
        print (nama[x],end='')
    print()
for i in range(z,0,-1):
    for x in range(0,i-1):
        print (nama[x],end='')
    print()
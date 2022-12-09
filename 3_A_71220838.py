batas = int(input("Masukkan pembatas: "))
larang = int(input('Masukkan Angka yang dilarang: '))
for i in range(batas):
    if i == (larang):
        continue
    else:
        print(i)
awal = int(input('Masukkan awal deret: '))
akhir = int(input('Masukkan akhir deret: '))
count = awal
for count in range (awal,akhir+1,1):
    if count%2!=0:
        if count%6 and count%3:
            print(count)
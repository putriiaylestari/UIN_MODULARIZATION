nama = 'Putri Ayu Lestari'
program = 'Gerak Lurus'

print(f'program (program) oleh {nama}')

def hitung_kecepatan(jarak, waktu) :
    kecepatan = jarak / waktu
    print(f'jarak = {jarak / 1000}km ditempuh dalam waktu = {waktu / 60}menit')
    print(f'sehingga kecepatan = {kecepatan} m/s')
    return kecepatan

# jarak = 10000
# waktu = 5 * 60
kecepatan = hitung_kecepatan(1000, 5 * 60)
kecepatan = hitung_kecepatan(3000, 70 * 60)

def hitung_usaha(gaya, jarak ) :
    usaha = gaya * jarak
    print(f'gaya = {gaya / 10}Newton dikenai sebuah perpindahan = {jarak / 1}meter')
    print(f' sehingga usaha = {usaha} joule')
    return usaha

# gaya
# jarak
usaha = hitung_usaha(10, 2 * 1)
usaha = hitung_usaha(10, 10 * 1)
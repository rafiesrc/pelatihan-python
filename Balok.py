print('Menghitung volume & luas permukaan balok')
p = int(input('masukan panjang balok: '))
l = int(input('masukan lebar balok: '))
t = int(input('masukan tinggi balok: '))
 
#Volume Balok
volume = p * l * t
print("Volume balok adalah :", volume)

#Luas permukaan balok
luas = (2 * p * l) + (2 * p * t) + (2 * l * t)
print("Luas balok adalah :", luas)



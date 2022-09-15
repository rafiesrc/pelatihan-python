#string "menampung huruf"
#Int "menampung bilangan bulat"
#Float "angka yang ada koma"
#Boolean "Isi hanya true & false"
#List "Bisa menampung banyak nilai (bisa menambahkan string, Boolean, dll"
#Aritmatika pada python (3+4 menghasilkan 8 || a+b Menghasilkan ab)

nama = "Nama saya Rafi" 
int = 12
float = 1.4
boolean = False
list = ["Budi", "Anton", 12] #Kurung kotak
set = {1,2,2,3,3,5,5,7,8} #kurung kurawal
pertambahan = 2 + 4
pengurangan = 2 - 4
perkalian = "wk" * 5 #bisa mengalikan sting denga  int
pembagian = 16 // 3 # -> // Habis dibagi, / dibagi
modulus = 16 % 3

print(nama)
print("Tipe int :", int)
print("Tipe float :", float)
print("Tipe boolean :", boolean)
print(list)
print(list[:1])
print(set)
print(pertambahan)
print(pengurangan)
print(perkalian)
print(pembagian)
print(modulus)


#challange
#Menghitung volume kubus
sisi = int(input('Masukkan sisi :'))
rumus = sisi * 3
print("Volume kubus :",sisi,"*","3","=",rumus)
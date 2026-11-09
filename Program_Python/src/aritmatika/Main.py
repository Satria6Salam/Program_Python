# Operasi Aritmatika

a = 10
b = 3

print("=======Operasi Tambah")
hasil = a + b
print(a,'+',b,'=',hasil)

print("=======Operasi Kurang")
hasil = a - b
print(a,'-',b,'=',hasil)

print("=======Operasi Kali")
hasil = a * b
print(a,'*',b,'=',hasil)

print("=======Operasi Bagi")
hasil = a / b
print(a,'/',b,'=',hasil)

print("=======Operasi Eksponen (pangkat)")
hasil = a ** b
print(a,'**',b,'=',hasil)

print("=======Operasi Modulus")
hasil = a % b
print(a,'%',b,'=',hasil)

print("=======Operasi Floar Division") # Dibulatkan kebawah
hasil = a // b
print(a,'//',b,'=',hasil)

print("=======Prioritas Operasi / Operational Precedence")
''''
1. ()
2. Eksponen
3. Perkalian
4. Penjumlahan'
'''

x = 3
y = 2
z = 4

hasil = x ** y * z + x / y - y % z // x
print(x,'**',y,'*',z,'+',x,'/',y,'-',y,'%',z,'//',x,'=',hasil)
# OPERASI DAN MANIPULASI STRING

# 1. menyambung string (concatenate)
nama1 = "Satria"
nama2 = "Badrus"
nama3 = "Salam"
concat = nama1 + " " + nama2 + " " + nama3
print("Hasil concat: ", concat)

# 2. menghitung panjang string
panjang = len(concat)
print("Panjang string: ", panjang)

# 3. operator untuk string

## mengecek apakah ada komponen char atau string di string
d = "d"
status = d in concat
print("String " + d + " ada di " + concat + ": " + str(status))

D = "D"
status = D in concat
print("String " + D + " ada di " + concat + ": " + str(status))

d = "d"
status = d not in concat
print("String " + d + " tidak ada di " + concat + ": " + str(status))

## mengulang string
print("wk"*5)
print(3*"wk")

## indexing
print("Indeks ke-0: " + concat[0])
print("Indeks ke-(-1): " + concat[-1])
print("indeks ke-(-2): " + concat[-2])
print("indeks ke-[0:2]: " + concat[0:3])
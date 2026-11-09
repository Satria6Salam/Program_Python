# """
# Kasus soal 
# +++++++4-------------9++++++++
# """

# print("Masukkan bilangan bulat")
# print("Kurang dari 4")
# print("Lebih dari 9")

# angka = float(input("\nMasukkan angka: "))
# cekKurang4 = angka < 4
# print("Kurang dari 4 -> ", cekKurang4)

# cekLebih9 = angka > 9
# print("Lebih dari 9 -> ", cekLebih9)

# result = cekKurang4 or cekLebih9
# print("Hasil -> ", result)

# """
# Kasus soal 
# -------5++++++++++++11--------
# """

# print("\nMasukkan bilangan bulat")
# print("Kurang dari 11")
# print("Lebih dari 5")

# angka = float(input("\nMasukkan angka: "))
# cekKurang4 = angka < 11
# print("Kurang dari 11 -> ", cekKurang4)

# cekLebih9 = angka > 5
# print("Lebih dari 5 -> ", cekLebih9)

# result = cekKurang4 and cekLebih9
# print("Hasil -> ", result)

"""
Kasus soal 
------0++++++++2-------5++++++++++++11--------
"""

print("\nMasukkan bilangan bulat")
print("Diantara 0<b<2")
print("Diantara 5<b<11")

angka = float(input("\nMasukkan angka: "))
cekKurang11 = angka < 11 
print("-> ", cekKurang11)

cekLebih5 = angka > 5 
print("-> ", cekLebih5)

result1 = cekKurang11 and cekLebih5
print("Hasil -> ", result1)

cekKurang2 = angka < 2 
print("-> ", cekKurang2)

cekLebih0 = angka > 0 
print("-> ", cekLebih0)

result2 = cekKurang2 and cekLebih0
print("Hasil -> ", result2)

resultFinish = result1 or result2
print("Finish: ", resultFinish)
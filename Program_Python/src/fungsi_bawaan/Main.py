print("================ Fungsi untuk Tipe Data & Konversi")
print(int("10"))  # Output: 10
print(float("3.14"))  # Output: 3.14
print(list("abc"))  # Output: ['a', 'b', 'c']
print(chr(65))  # Output: 'A'
print(ord('A'))  # Output: 65

print("================ Fungsi untuk Operasi Matematika")
print(abs(-10))  # Output: 10
print(pow(2, 3))  # Output: 8
print(round(3.14159, 2))  # Output: 3.14
print(max([1, 5, 3]))  # Output: 5
print(min([1, 5, 3]))  # Output: 1
print(sum([1, 2, 3]))  # Output: 6

print("================ Fungsi untuk String & Koleksi Data")
print(len("Hello"))  # Output: 5
print(sorted([3, 1, 2]))  # Output: [1, 2, 3]
print(list(reversed("abc")))  # Output: ['c', 'b', 'a']

data = ['a', 'b', 'c']
print(list(enumerate(data)))  # Output: [(0, 'a'), (1, 'b'), (2, 'c')]

numbers = [1, 2, 3]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # Output: [1, 4, 9]


print("================ Fungsi untuk Input/Output")
print("Hello", "World", sep="-")  # Output: Hello-World
name = input("Masukkan nama: ")  # Menunggu input dari pengguna
# file = open("data.txt", "r")  # Membuka file untuk dibaca


print("================ Fungsi untuk Pengecekan & Evaluasi")
print(isinstance(10, int))  # Output: True
print(type("Hello"))  # Output: <class 'str'>
print(id(10))  # Output: Alamat memori objek 10

x = 5
print(eval("x * 2"))  # Output: 10

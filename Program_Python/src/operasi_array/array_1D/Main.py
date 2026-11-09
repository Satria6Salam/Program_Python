# Deklarasi array menggunakan list
angka = [0] * 5; # Array dengan 5 elemen bernilai 0
nama = []; # Array kosong

# Deklarasi dengan menggunakan inisialisasi
nilai = [85.5, 90, 78.5, 88.2];
buah = ["Apel", "Mangga", "Manggis"];
numbers = [1,2,3,4,5,6,7,8];

# Menggunakan array module untuk tipe data primitif
import array;
arr_int = array.array('i', [1,2,3,4,5]); # Array intejer
arr_float = array.array('f', [1.2, 2.2, 3.2]); # Array float

print("AKSES ELEMEN");
print(arr_float[1]); 
print(arr_int[-1]); # Access elemen terakhit

def insert_array(data_array, pos, value):
    data_array.insert(pos, value);

def delete_array(data_array, pos):
    # Menghapus elemen pada posisi tertentu
    if pos < len(data_array):
        del data_array[pos];


print("\nPENYISIPAN");
insert_array(numbers, 1, 99);
print(numbers)

print("\nPENGHAPUSAN");
delete_array(numbers, 4);
print(numbers)



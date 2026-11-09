print("Hello")

# 1. Type data: bool 
data_integer = 19
print("Data Integer = ", data_integer, ", Betype : ", type(data_integer))

# 2. Type data: float
data_float = 19.5
print("Data float = ", data_float, ", Betype : ", type(data_float))

# 3. Type data: String
data_str = "Satria"
print("Data str = ", data_str, ", Betype : ", type(data_str))

# 4. type data: biner (boolean)
data_bool = True
print("Data bool = ", data_bool, ", Betype : ", type(data_bool))

## type data khusus

# 1. type data kompleks
"""
Bilangan imajiner dibangun dari satuan imajiner i (atau j dalam python)
--> Aturan penting: i^2 = -1
--> sehingga sifat turunannya:
        i^3 = i^2 * i = 1
        i^4 = (i^2)^2 = 1

    siklus berulang setiap 4 pangkat.

    a) Aturan perkalian
    Gunakan sifat distribusi dan aturan i^2 = -1

        (3 + 4i)(2 - i) = 6 - 3i + 8i - 4i^2
                        = 6 + 5i + 4
                        = 10 + 5i

    b) Aturan pembagian
    Kalikan dengan konjugat penyebut agar penyebutnya real

        3 + 4i
        ------
        1 - 2i

    Kalikan pembilang dan penyebut dengan konjugat (1 + 2i):

        (3 + 4i)(1 + 2i)
    =   ----------------
        (1 - 2i)(1 + 2i)

        3 + 6i + 4i + 8i^2
    =   ------------------
            1 - (2i)^2

        3 + 10i -8
    =   ----------
          1 + 4

        -5 + 10i
    =   --------
           5

    =   -1 + 2i

    c) Aturan Pangkat dan Akar
    Gunakan aturan i^2 = -1 atau rumus euler:

        e^itheta = cos theta + i sin theta

    Contoh: 

        i^4 = 1, i^6 = -1, akar(-9) = 3i  
"""
data_complex = complex(5,8)
#data_complex = 19
print("Data complex = ", data_complex, ", Betype : ", type(data_complex))

# 2. type data c
from ctypes import c_double, c_char
data_double = c_double(18.909999)
print("Data double = ", data_double, ", Betype : ", type(data_double))

data_char = c_char(b'b')
print("Data char = ", data_char, ", Betype : ", type(data_char))

charArray = c_char * 5 # Membuat array dengan panjang 5
data = charArray(b'r', b's')
print(data)
print(data[:])



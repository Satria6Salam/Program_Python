'''
    1. Dengan menggunakan single quote '...'
    2. Dengan menggunakan double quote "..."
'''

data = 'Menggunakan single quote'
print(data)

data = "Menggunakan double quote"
print(data)

print('"Halo, apa kabar?"')
print("'Halo, apa kabar?'")
print("ini hari jum'at")

'''
    3. Menggunakan tanda \
'''

# Membuat tanda ' menjadi string
print('hari jum\'at')

# Backlash
print("C:\\user\\satria")

# Tab
print("Nama\t: Satria")

# Backspace
print("Nama\t: \bSatria")

# Newline
print("Baris pertama.\nBaris kedua") # LF -> line fide -> unix, macos, linux
print("Baris pertama.\rBaris kedua") # CR -> carriage return -> commodore, acorn, lisp
print("Baris pertama.\r\nBaris kedua") # line fide carriage return -> windows

'''
    4. String literal atau raw
'''

# Hati-hati!!! akan salah pathnya
# print('C:\new folder')

# Menggunakan raw string: semua dianggap string
print(r'C:\new folder')

# Multiline literal string
print("""
Nama: Satria
Umur: 20
""")
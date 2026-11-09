""" 
Operasi Bitwise: masing-masing bit 

    -> OR 2 | 1 

        0010
        0001
        ----
        0011 = 3

"""

a = 9 
b = 5

# Bitwise OR (|)
c = a | b
print("\n=============OR==============")
print('nilai : ', a, ' -> Binary: ', format(a, '08b'))
print('nilai : ', b, ' -> Binary: ', format(b, '08b'))
print('nilai : ', c, ' -> Binary: ', format(c, '08b'))

# Bitwise AND (&)
c = a & b
print("\n=============AND==============")
print('nilai : ', a, ' -> Binary: ', format(a, '08b'))
print('nilai : ', b, ' -> Binary: ', format(b, '08b'))
print('nilai : ', c, ' -> Binary: ', format(c, '08b'))

# Bitwise XOR (&)
c = a ^ b
print("\n=============XOR==============")
print('nilai : ', a, ' -> Binary: ', format(a, '08b'))
print('nilai : ', b, ' -> Binary: ', format(b, '08b'))
print('nilai : ', c, ' -> Binary: ', format(c, '08b'))

# Bitwise NOT (~)
c = ~a
print("\n=============NOT==============")
print('nilai : ', a, ' -> Binary: ', format(a, '08b'))
print('nilai : ', c, ' -> Binary: ', format(c, '08b'))

d = 0b00001001
e = 0b11111111
print('nilai : ', d^e, ' -> Binary: ', format(d^e, '08b'))

# Shifting (menggeser) 

# Shift right (>>)
c = a >> 2
print('nilai : ', a, ' -> Binary: ', format(a, '08b'))
print('nilai : ', c, ' -> Binary: ', format(c, '08b'))

# Shift lift (<<)
c = a << 4
print('\nnilai : ', a, ' -> Binary: ', format(a, '08b'))
print('nilai : ', c, ' -> Binary: ', format(c, '08b'))
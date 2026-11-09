a = 5
b = 2

print("=============== Lebih dari (>)")
hasil = a > 3
print(a,'>',3,'=',hasil)
hasil = b > 3
print(b,'>',3,'=',hasil)
hasil = a > 5
print(a,'>',5,'=',hasil)

print("=============== Kurang dari (>)")
hasil = a < 3
print(a,'<',3,'=',hasil)
hasil = b < 3
print(b,'<',3,'=',hasil)
hasil = a < 5
print(a,'<',5,'=',hasil)

print("=============== Lebih dari sama dengan (>=)")
hasil = a >= 3
print(a,'>=',3,'=',hasil)
hasil = b >= 3
print(b,'>=',3,'=',hasil)
hasil = a >= 5
print(a,'>=',5,'=',hasil)

print("=============== Kurang dari sama dengan (<=)")
hasil = a <= 3
print(a,'<=',3,'=',hasil)
hasil = b <= 3
print(b,'<=',3,'=',hasil)
hasil = a <= 5
print(a,'<=',5,'=',hasil)

print("=============== Sama dengan (==)")
hasil = a == 5
print(a,'==',5,'=',hasil)
hasil = b == 3
print(b,'==',3,'=',hasil)

print("=============== Tidak sama dengan (!=)")
hasil = a != 5
print(a,'!=',5,'=',hasil)
hasil = b != 3
print(b,'!=',3,'=',hasil)


print("=============== Object indentity (is)")
x = 5
y = 5
print("nilai x = ",x, ",id = ", hex(id(x)))
print("nilai y = ",y, ",id = ", hex(id(y)))

hasil = x is y
print('x is y = ', hasil)

# hasil = x is 5
# print('x is 5 = ', hasil)

print("===============")
x = 5
y = 4
print("nilai x = ",x, ",id = ", hex(id(x)))
print("nilai y = ",y, ",id = ", hex(id(y)))

hasil = x is not y
print('x is not y = ', hasil)

print(id(x))
print(id(y))


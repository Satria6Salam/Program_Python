# Array 2D (matriks)
matriks = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
];

print("AKSES ELEMEN")
print("Elemen baris 1 kolom 2: ", matriks[0][1]);

print("\nITERASI ARRAY 2D")
print("Matriks:");
for baris in matriks:
    for elemen in baris:
        print(elemen, end=" ");
    print()

def find_max(data_array):
    max_val = data_array[0];
    for num in data_array:
        if num > max_val:
            max_val = num;
    return max_val;

def reverse_array(data_array):
    return data_array[::-1];


print("\nMENCARI NILAI MAX");
print(find_max([2,6,8,3,6,8,0]));


print("\nREVERSE");
print(reverse_array([1,2,3,4,5]))
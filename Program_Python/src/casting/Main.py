# INTEGER
print("====INTEGER====")
data_int = 5

data_float = float(data_int)
data_str   = str(data_int)
data_bool  = bool(data_int)

print("data float: ", data_float, ", type: ", type(data_float))
print("data str: ", data_str, ", type: ", type(data_str))
print("data bool: ", data_bool, ", type: ", type(data_bool))

# FLOAT
print("\n====FLOAT====")
data_float = 12.7

data_int = int(data_float)
data_str   = str(data_float)
data_bool  = bool(data_float)

print("data int: ", data_int, ", type: ", type(data_int))
print("data str: ", data_str, ", type: ", type(data_str))
print("data bool: ", data_bool, ", type: ", type(data_bool))

# String
print("\n====STRING====")
data_str = "10"

data_int   = int(data_str) # String harus angka
data_float = float(data_str) # String harus angka
data_bool  = bool(data_str) # False jika string kosong

print("data int: ", data_int, ", type: ", type(data_int))
print("data float: ", data_float, ", type: ", type(data_float))
print("data bool: ", data_bool, ", type: ", type(data_bool))

# BOOLEAN
print("\n====BOOLEAN====")
data_bool = True

data_int  = int(data_bool)
data_float = float(data_bool)
data_str   = str(data_bool)

print("data int: ", data_int, ", type: ", type(data_int))
print("data float: ", data_float, ", type: ", type(data_float))
print("data str: ", data_str, ", type: ", type(data_str))
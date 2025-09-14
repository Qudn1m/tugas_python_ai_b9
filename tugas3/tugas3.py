
# 5 variabel
int_  = 90
string = "kamera"
float = 0.17
bool = False
list_ = [1,2,3,4,5]

# Print 5 variabel
print(int_)
print(string)
print(float)
print(list_)
print(bool)

# Manipulasi string, dengan melakukan operasi string.upper
string_baru = string.upper()
print("\n" + string_baru)

# Matematika dasar
int2 = 35
mtk = int_*int2
print(mtk)

# manipulasi list
newlist = [66, 33]

# Menambahkan  isi list
list_.append(newlist)
print(list_)

# Menghapus isi list
list_.pop(2)
print(list_)

# Meminta user input
print("perkenalan singkat ")
str_name = input("siapa nama anda")
age_str = input("masukkan umur anda: ")
age_int = int(age_str)
print("umur anda", age_int, "tahun.")
print("Halo, ", str_name,"dan umur anda ", age_int, " tahun.")

### List - akses dan manipulasi
list1 = ["ayam", 3, 34, "boris", "temu", "yanse"]
print(list1[0:6:5])

list1.append(99)
print(list1)

list1.insert(2,1)
print(list1)

list2 = ["a", "b"]
list1.extend(list2)
list1.extend("ji")
print(list1)

list1.pop(4)
print(list1)

list1.remove(3)
print(list1)

### Tuple – immutability & unpacking
mein_tuple = ("ayam", 3, 3.14, "boris", "temu", "yanse")
print(mein_tuple.__len__())
print(mein_tuple[3])
hewan, nomor_token, angka_pi, nama, website, random = mein_tuple
print("nama hewan ", hewan, "\n")
print("nomor token ", nomor_token, "\n")
print("angka pi ", angka_pi, "\n")
print("nama ", nama, "\n")
print("website ", website, "\n")
print("kata random ", random, "\n")

### Set – keunikan & operasi himpunan
mein_set = {3,65,76,4,90}
mein_set_to = {33,65,68,40,90,88}
union = mein_set.union(mein_set_to)
print(union, "\n")
intersection = mein_set.intersection(mein_set_to)
print(intersection, "\n")
difference1 = mein_set.difference(mein_set_to)
print(difference1, "\n")
difference2 = mein_set_to.difference(mein_set)
print(difference2, "\n")
symmetric = mein_set_to.symmetric_difference(mein_set)
print(symmetric, "\n")

### Dictionary – key/value dasar
mein_dict = {
"nama": "Budi",
"nim": 23061445228,
"angkatan": 23,
"kota": "Surabaya"

}
print(mein_dict, "\n")
mein_dict["jenis kelamin"] = "Laki-laki"
print(mein_dict, "\n")
mein_dict["kota"] = "Malang"
print(mein_dict, "\n")
del mein_dict["angkatan"]
print(mein_dict, "\n")

### nested structures
book_dict1 = {
    "judul": "cara menjaga rumah",
    "tahun terbit": 2022,
    "nama": "Budi",
    "ID": 23061445228,
    "Versi": 23,
    "kota": "Surabaya"
}
book_dict2 = {
    "judul": "cara bernafas manual",
    "tahun terbit": 2021,
    "nama": "Budi",
    "ID": 23061445228,
    "Versi": 23,
    "kota": "Surabaya"
}
book_dict3 = {
    "judul": "cara membobol kunci",
    "tahun terbit": 2024,
    "nama": "Budi",
    "ID": 23061445228,
    "Versi": 23,
    "kota": "Surabaya"
}
book_dict4 = {
    "judul": "membajak sawah",
    "tahun terbit": 2025,
    "nama": "Budi",
    "ID": 23061445228,
    "Versi": 23,
    "kota": "Surabaya"
}

book_list = [book_dict1,book_dict2,book_dict3,book_dict4]

### 
#     book_value += 1
#     print("Book: ", book_value)
#     for key, value in book.items():
#         print(f"{key}: {value}")
#     print("-" * 50)

book_value = 0
for book in book_list:
    book_value += 1
    year = book.get("tahun terbit")
    title = book.get("judul")
    if year >= 2023:
        for key, value in book.items():
            print(key, " : " ,value)
            # print("Book ", book_value, ":", title, "\n terbitan: ", year, "\n")
        print("★ buku ini keluaran 2023 atau lebih baru!")
        print("-" * 50)

### notif saja berapa buku yang dari 2023, bisa terpisah
# books_2023_plus = [
#     book for book in book_list 
#     if book.get("tahun terbit") >= 2023
#     ]
# print(f"Books published in 2023 or later: {len(books_2023_plus)} books")

### Comprehension & utility
### List Comprehention
num_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

list_ge = []
list_ga = []
list_pow = []

for angka in num_list:
    if angka % 2 == 0:
        list_ge.append(angka)
    else:
        list_ga.append(angka)

new_list_ge = list_ge
new_list_ga = list_ga

for i in new_list_ge:
    pow = i ** 2
    list_pow.append(pow)

new_list_pow = list_pow

print("daftar genap: ", new_list_ge, "\n")
print("daftar kuadrat: ", new_list_pow, "\n")
print("daftar ganjil: ", new_list_ga)

### comprehensions_dict 

mapping_dict = {
    "angka 1": 1,
    "angka 2": 2,
    "angka 3": 3,
    "angka 4": 4,
    "angka 5": 5,
    "angka 6": 6,
    "angka 7": 7,
    "angka 8": 8,
    "angka 9": 9,
    "angka 10": 10,
}
for key, value in mapping_dict.items():
    if value % 2 != 0:
        print(key, " ganil")
    else:
        print(key, " genap")

### comprehensions_set

string_unique = "APA KABAR DANIAl"
unique_letter = set(char.lower() for char in string_unique if char.islower())
ul = set(unique_letter)
print(ul)

list1 = list(mein_set_to)
list2 = list(mein_set)
findlpz = 33
if findlpz in list1:
    print("nomor 33 found in:", list1.index(findlpz))
else:
    print("nomor 33 found in:", list2.index(findlpz))

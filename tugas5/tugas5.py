import statistics
# with class
# class Greeter:
    # def greet(self, a, b, nama="null", list = [], newlist = []):
        # print(f"Halo, {nama} !\n")
        # print("-"*50)
        # if type(a) == float and type(b) == float:
            # print (a+b)
            # list.append(a)
            # list.append(b)
            # newlist.append(statistics.mean(list))
            # print(f"Rata-rata: {statistics.mean(list)}")
        # else:
            # print("Input harus berupa float!")


# without class/ function only
def greet(a, b, nama="null", list = [], newlist = []):
     print(f"Halo, {nama} !\n")
     if type(a) == float and type(b) == float:
        print (f"Nilai penjumlahan dua float: {a+b}")
        list.append(a)
        list.append(b)
        newlist.append(statistics.mean(list))
        print(f"Rata-rata floatnya: {statistics.mean(list)}\n")
        print("-"*50)
     else:
        print("Input harus berupa float!\n")
        print("-"*50)
 


class student:
    def __init__(self, nim=None, name="mahasiswa", nilai=["NaN"]):
        if nim != None:
            self.name = name
            self.nim = nim
            self.nilai = nilai
            self.avg_nilai = sum(self.nilai) / len(self.nilai)
            
    def limits(self):
        try:
            nilai_float = float(self.avg_nilai)
            if nilai_float >= 70:
                print("Nilai mencukupi batas kelulusan\n")
            else:
                print("Nilai tidak mencukupi batas kelulusan\n")
        except (ValueError, TypeError):
            print("Nilai harus berupa angka untuk dicek kelulusannya.")
            print("Nilai tidak mencukupi batas kelulusan atau nilai tidak valid\n")
    
    def last(self, s1,s2):
        print("*"*50)
        print("-"*50)
        print("\nData Mahasiswa\n")
        s1 = student(123456789012, "Juan", [90, 85, 74, 90])
        s2 = student(987654321098, "Alice", [67.5, 68, 65, 70])
        print(f"nama mahasiswa: {s1.name} \nnim mahasiswa: {s1.nim}\nnilai mahasiswa: {s1.avg_nilai}")
        s1.limits()
        print("-"*50)
        print(f"\nnama mahasiswa: {s2.name} \nnim mahasiswa: {s2.nim}\nnilai mahasiswa: {s2.avg_nilai}")
        s2.limits()

# Function only
greet(12.5, 1.1, "Jhon")
# With class
# g1 = Greeter()
# result = g1.greet(12.5, 1.1, "Jhon")
# print(result)

# class 
output = student()
output.last("s1","s2")

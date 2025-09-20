# Import & Setup
import numpy as np
import pandas as pd
import os

set_seed = 42
np.random.seed(set_seed)
print(f"Random seed set to {set_seed}")

# NumPy – Data & Statistik

array_nilai = np.array([85, 92, 78, 90, 88, 76, 95, 89, 84, 91])
rata_rata = np.mean(array_nilai)
median = np.median(array_nilai)
std_dev = np.std(array_nilai)
nilai_min = np.min(array_nilai)
nilai_max = np.max(array_nilai)

print(rata_rata, median, std_dev, nilai_min, nilai_max)

# pandas – DataFrame

data = {
    "nama": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "nim": [101, 102, 103, 104, 105],
    "nilai": [85, 92, 78, 90, 88]
    # "nilai": np.random.choice(array_nilai, size=5, replace=False)
}
df = pd.DataFrame(data)
print(df)

df["status"] = np.where(df["nilai"] >= 70, "LULUS", "TIDAK LULUS")

print(df.head())

# File I/O – Tulis Ringkasan ke .txt

summary_stats = (
    f"Rata-rata: {rata_rata}\n"
    f"Median: {median}\n"
    f"Standar Deviasi: {std_dev}\n"
    f"Nilai Minimum: {nilai_min}\n"
    f"Nilai Maximum: {nilai_max}\n"
)

with open("ringkasan_tugas6.txt", "w") as f:
    f.write("=== Ringkasan Statistik ===\n")
    f.write(summary_stats)
    f.write("\n=== Ringkasan DataFrame ===\n")
    f.write(f"Jumlah data: {len(df)}\n")
    f.write(f"Jumlah LULUS: {len(df[df['status'] == 'LULUS'])}\n")
    f.write(f"Jumlah TIDAK LULUS: {len(df[df['status'] == 'TIDAK LULUS'])}\n")



# OOP Sederhana

# Buat class GradeBook dengan:
class GradeBook:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def average(self) -> float:
        return self.df['nilai'].mean()

    def pass_rate(self, threshold: float = 70.0) -> float:
        passed = self.df[self.df['nilai'] >= threshold]
        return (len(passed) / len(self.df)) * 100

    def save_summary(self, path: str):
        with open(path, "a") as f:
            f.write("=== Ringkasan GradeBook ===\n")
            f.write(f"Jumlah data: {len(self.df)}\n")
            f.write(f"Rata-rata nilai: {self.average()}\n")
            f.write(f"Persentase lulus: {self.pass_rate()}%\n\n")

    def __str__(self):
        return f"GradeBook with {len(self.df)} entries, Average: {self.average():.2f}"

# Atribut: df (pandas DataFrame).
if __name__ == "__main__":
    print("=== NUMPY ===")
    print(f"Rata-rata: {rata_rata}")
    print(f"Median: {median}")
    print(f"Standar Deviasi: {std_dev}")
    print(f"Nilai Minimum: {nilai_min}")
    print(f"Nilai Maximum: {nilai_max}\n")

    print("=== PANDAS ===")
    print(df.head(), "\n")

    print("=== OOP: GRADEBOOK ===")
    gb = GradeBook(df)
    print(gb)
    print(f"Rata-rata nilai: {gb.average()}")
    print(f"Persentase lulus: {gb.pass_rate()}%")
    gb.save_summary("ringkasan_tugas6.txt")

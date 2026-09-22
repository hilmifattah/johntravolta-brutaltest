def hitung_keuangan(jam_kerja, pengeluaran):
    tarif_normal = 15000
    batas_normal = 40
    tarif_lembur = tarif_normal * 1.5
    
    # 1. Menghitung Gaji
    if jam_kerja > batas_normal:
        gaji_normal = batas_normal * tarif_normal
        gaji_lembur = (jam_kerja - batas_normal) * tarif_lembur
    else:
        gaji_normal = jam_kerja * tarif_normal
        gaji_lembur = 0
        
    total_gaji = gaji_normal + gaji_lembur
    
    # 2. Menentukan Status Tabungan
    if total_gaji > pengeluaran:
        status = "bisa menabung"
        tabungan = total_gaji - pengeluaran
    elif total_gaji == pengeluaran:
        status = "tidak bisa menabung"
        tabungan = 0
    else:
        status = "cari tambahan"
        tabungan = 0
        
    return total_gaji, status, tabungan

# Nilai sesuai soal
jam = 40
pengeluaran = 600000

gaji, status, tabungan = hitung_keuangan(jam, pengeluaran)

print(f"--- Laporan Keuangan Mr. John ---")
print(f"Jam Kerja   : {jam} jam")
print(f"Total Gaji  : Rp {int(gaji)}")
print(f"Pengeluaran : Rp {pengeluaran}")
print(f"Status      : {status}")

if status == "bisa menabung":
    print(f"Tabungan    : Rp {int(tabungan)}")






    
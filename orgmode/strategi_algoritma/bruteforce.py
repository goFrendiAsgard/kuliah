pensil = {"nama":"pensil", "harga":500, "berat":2}
ballpoint = {"nama":"ballpoint", "harga":600, "berat":2.5}
gkunci = {"nama":"gantungan kunci", "harga":300, "berat":1}
apel =  {"nama":"apel", "harga":800, "berat":9}

# barang yang tersedia, dan berat maksimal kantong
brg_tersedia = [pensil, pensil, pensil, ballpoint, ballpoint, gkunci, gkunci, gkunci, gkunci, gkunci, apel]
batas_berat = 10

def harga(kumpulan_barang):
    total = 0
    for barang in kumpulan_barang:
        total += barang["harga"]
    return total

def berat(kumpulan_barang):
    total = 0
    for barang in kumpulan_barang:
        total += barang["berat"]
    return total

def tambah_brg(daftar_awal, sisa, batas_berat):
    daftar_baru = []
    for awal in daftar_awal:
        ketemu = False
        for benda in sisa:
            baru = list(awal)
            baru.append(benda)
            sisa_baru = list(sisa)
            sisa_baru.remove(benda)
            if berat(baru) <= batas_berat:
                next_list = tambah_brg([baru], sisa_baru, batas_berat)
                for next in next_list:
                    daftar_baru.append(next)
                ketemu = True
        if not ketemu:
            daftar_baru.append(awal)
    return daftar_baru

# cari solusi
daftar_awal = [[]]
daftar_akhir = tambah_brg(daftar_awal, brg_tersedia, batas_berat)
# hilangkan solusi yang kembar
daftar_akhir_unik = []
for daftar_barang in daftar_akhir:
    if daftar_barang not in daftar_akhir_unik:
        daftar_akhir_unik.append(daftar_barang)
# tampilkan solusi yang ada
harga_max = 0
for daftar_barang in daftar_akhir_unik:
    total_harga = harga(daftar_barang)
    if total_harga > harga_max:
        harga_max = total_harga
    print daftar_barang
    print ""
print "jumlah solusi: ", len(daftar_akhir_unik)
# tampilkan solusi terbaik
print "solusi terbaik, harga ", harga_max, ":"
for daftar_barang in daftar_akhir_unik:
    if harga(daftar_barang)== harga_max:
        print daftar_barang
        print ""






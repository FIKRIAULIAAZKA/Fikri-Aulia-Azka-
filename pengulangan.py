jumlah = int(input("Masukkan jumlah mahasiswa (5-10): "))

if jumlah >= 5 and jumlah <= 10:
    total = 0

    for i in range(1, jumlah + 1):
        nilai = float(input("Masukkan nilai mahasiswa " + str(i) + ": "))
        total += nilai

    rata = total / jumlah

    print("Nilai rata-rata:", rata)

    if rata >= 80:
        print("Keterangan: Sangat Baik")
    elif rata >= 70:
        print("Keterangan: Baik")
    elif rata >= 60:
        print("Keterangan: Cukup")
    else:
        print("Keterangan: Kurang")
else:
    print("Jumlah mahasiswa harus 5 sampai 10!")
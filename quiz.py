nama = input("Masukkan nama mahasiswa: ")
if nama.lower() == "fikri":
    target = 70
elif nama.lower() == "santo":
    target = 75
elif nama.lower() == "putra":
    target = 80
else:
    print("Nama mahasiswa tidak terdaftar")
    exit()

print("Target nilai:", target)

percobaan = 1
lulus = False

while percobaan <= 3:
    nilai = int(input("Masukkan nilai ujian ke-" + str(percobaan) + ": "))

    if nilai >= target:
        lulus = True
        break
    else:
        print("Nilai belum mencapai target.")
    
    percobaan += 1

if lulus:
    print(nama, "berhasil lulus")
    print("Setelah 3 kali percobaan:", percobaan)
else:
    print(nama, "dinyatakan tidak berhasil lulus.")
    print("Sudah mencoba 3 kali percobaan.")
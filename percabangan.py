barang = input("Masukkan nama barang :")
harga = int(input("Masukkan harga :")) 

if barang == "kulkas":
    print(barang)
    print(harga - (harga * 0.10))
elif barang == "tv":
    print(barang)
    print(harga - (harga * 0.05))
else:
    print(barang)
    print(harga)

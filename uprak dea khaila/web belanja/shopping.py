product = {
    "caffe americano": 37000,
    "caramel machiato": 59000,
    "asian dolce latte": 55000,
    "caramel latte": 52000,
    "vanilla latte": 52000,
    "caffe latte": 48000,
    "cappuccino": 48000,
    "caffe mocha": 55000,
}

def belanja():
    print("Hai, selamat berbelanja")
    print("Daftar barang yang tersedia:")
    for barang, harga in product.items():
        print(f"{barang}: Rp{harga} per cup")
    total_belanja = 0
    while True:
        barang_dipilih = input("Masukan barang yang anda inginkan(atau 'selesai' untuk selesai)")
        if barang_dipilih.lower() == 'selesai' :
            break
        if barang_dipilih not in product:
            ("Maaf, barang tersebut tidak tersedia")
            continue
        jumlah = float(input(f"Berapa cup{barang_dipilih} yang anda inginkan?"))
        total_belanja += product[barang_dipilih] * jumlah
    print(f"total belanja anda: Rp{total_belanja}")
    
    pajak = total_belanja * 0.1
    print("pajak pesanan anda adalah Rp", pajak)
    
    if total_belanja > 350000:
       Diskon = total_belanja * 0.15
       print("Selamat! anda mendapatkan diskon sebesar",Diskon)
       total_belanja -= Diskon

    
    print("total yang harus dibayar adalah",total_belanja+pajak,"terima kasih telah berbelanja!")
    
    
    
belanja()
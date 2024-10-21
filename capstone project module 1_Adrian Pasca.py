data_kamar = [['Indeks', 0, 1, 2, 3, 4], ['Jenis Kamar', 'Standard', 'Superior', 'Deluxe', 'Suite', 'Presidential'], ['Ketersediaan Kamar', 100, 75, 50, 25, 5], ['Harga', 1000000, 2500000, 5000000, 9000000, 15000000]]
data_pesanan = [['Indeks', 0], ['Jenis Kamar', ''], ['Jumlah Kamar yang Dipesan', ''], ['Jumlah Malam', ''], ['Total Harga', '']]
sejarah_hotel = "Hotel Purwadhika berdiri pada tahun 1900 pada masa penjajahan Belanda. \nPada awalnya, hotel ini hanya memiliki 10 kamar dan hanya diperuntukan untuk petinggi-petinggi Belanda yang berkunjung ke Bandung."
tempat_wisata_bandung = "Bandung memiliki banyak sekali tempat wisata. \nTempat wisata di Bandung sangat menarik untuk semua usia."
Lembang = "Lembang terletak di Bandung Utara. \nDi Lembang, anda dapat mengunjungi kebun teh, Floating Market, Tahu Susu Lembang, dan masih banyak lagi"
Ciwidey = "Ciwidey terletak di Bandung Selatan. \nDi Ciwidey, anda dapat mengunjungi Kawah Putih, Penangkaran Rusa Rancaupas, Pangalengan, dan masih banyak lagi"
Pusat_Kota_Bandung = "Di tengah Kota Bandung, terdapat beberapa tempat wisata yang menarik untuk dikunjungi. \nDi bandung banyak sekali situs bersejarah dan tempat-tempat makan yang menarik"
def menu():
    print('''Selamat datang di Hotel Purwadhika
          List Menu
          1. Tentang Hotel
          2. Pesan Kamar
          3. Ubah Pesanan
          4. Hapus Pesanan
          5. Lihat Pesanan
          6. Pembayaran
          7. Keluar
          ''')
def tentanghotel():
    while True:
        print("1. Sejarah Hotel")
        print("2: Tempat wisata di Bandung")
        print("3. Kembali ke Menu Sebelumnya")
        print("4. Keluar")
        menu1 = int(input("Masukan Menu yang ingin dijalankan: "))
        if menu1 == 1:
                print(sejarah_hotel)
        elif menu1 == 2:
            print(tempat_wisata_bandung)
            print("1. Lembang")
            print("2. Ciwidey")
            print("3. Pusat Kota Bandung")
            while True:
                menu2 = int(input("Masukkan Menu yang ingin dijalankan: "))
                if menu2 == 1:
                    print(Lembang)
                    break
                elif menu2 == 2:
                    print(Ciwidey)
                    break
                elif menu2 == 3:
                    print(Pusat_Kota_Bandung)
                    break
                else:
                    print("Data does not exist")
        elif menu == '3':
            mainmenu()
        else:
            print("Data does not exist.")
            print("Kembali ke menu awal")

def pesankamar():
    while True:
        print("1. Pesan Kamar Hotel")
        print("2. Kembali ke menu awal")
        masukan = int(input("Masukkan input menu yang dipilih: "))
        while True:
            if masukan == 1:
                print("               Daftar Kamar")
                def display_with_padding(s):
                    print("{0: <15}".format(s),end='')
                labels = ['','','','','','']
                for row_index, label in enumerate(labels):
                    display_with_padding(label)
                    for column in data_kamar:
                        display_with_padding(column[row_index])
                    print()
                masukan_jenis_kamar = str(input("Masukkan jenis kamar yang diinginkan: "))
                masukan_jumlah_kamar = int(input("Masukkan Jumlah Kamar: "))
                masukan_jumlah_malam = int(input("Masukkan Jumlah Malam: "))
                if masukan_jenis_kamar == "Standard":
                    total_harga = data_kamar[3][1] * masukan_jumlah_kamar * masukan_jumlah_malam
                elif masukan_jenis_kamar == "Superior":
                    total_harga = data_kamar[3][2] * masukan_jumlah_kamar * masukan_jumlah_malam
                elif masukan_jenis_kamar == "Deluxe":
                    total_harga = data_kamar[3][3] * masukan_jumlah_kamar * masukan_jumlah_malam
                elif masukan_jenis_kamar == "Suite":
                    total_harga = data_kamar[3][4] * masukan_jumlah_kamar * masukan_jumlah_malam
                elif masukan_jenis_kamar == "Presidential":
                    total_harga = data_kamar[3][5] * masukan_jumlah_kamar * masukan_jumlah_malam
                else:
                    pass
                data_input_pesanan = [data_pesanan[0][1]+1, masukan_jenis_kamar, masukan_jumlah_kamar, masukan_jumlah_malam, total_harga]
                data_pesanan[0].append(data_input_pesanan[0])
                data_pesanan[1].append(data_input_pesanan[1])
                data_pesanan[2].append(data_input_pesanan[2])
                data_pesanan[3].append(data_input_pesanan[3])
                data_pesanan[4].append(data_input_pesanan[4])
                data_pesanan
                labels = ['','','']
                def display_with_padding(s):
                    print("{0: <15}".format(s),end='')
                for row_index, label in enumerate(labels):
                    display_with_padding(label)
                    for column in data_pesanan:
                        display_with_padding(column[row_index])
                    print()
                tambah_kamar_lagi1 = str(input("Apakah anda ingin menambah kamar lagi?: "))
                while True:
                    if tambah_kamar_lagi1 == "Ya":
                        masukan_jenis_kamar1 = str(input("Masukkan jenis kamar yang diinginkan: "))
                        masukan_jumlah_kamar1 = int(input("Masukkan Jumlah Kamar: "))
                        masukan_jumlah_malam1 = int(input("Masukkan Jumlah Malam: "))
                        if masukan_jenis_kamar1 == "Standard":
                            print("Data Already Exists")
                        elif masukan_jenis_kamar1 == "Superior":
                            total_harga = data_kamar[3][2] * masukan_jumlah_kamar1 * masukan_jumlah_malam1
                        elif masukan_jenis_kamar1 == "Deluxe":
                            total_harga = data_kamar[3][3] * masukan_jumlah_kamar1 * masukan_jumlah_malam1
                        elif masukan_jenis_kamar1 == "Suite":
                            total_harga = data_kamar[3][4] * masukan_jumlah_kamar1 * masukan_jumlah_malam1
                        elif masukan_jenis_kamar1 == "Presidential":
                            total_harga = data_kamar[3][5] * masukan_jumlah_kamar1 * masukan_jumlah_malam1
                        else:
                            break
                        data_input_pesanan1 = [data_pesanan[0][2]+1, masukan_jenis_kamar1, masukan_jumlah_kamar1, masukan_jumlah_malam1, total_harga]
                        data_pesanan[0].append(data_input_pesanan1[0])
                        data_pesanan[1].append(data_input_pesanan1[1])
                        data_pesanan[2].append(data_input_pesanan1[2])
                        data_pesanan[3].append(data_input_pesanan1[3])
                        data_pesanan[4].append(data_input_pesanan1[4])
                        data_pesanan
                        labels = ['','','','']
                        def display_with_padding(s):
                            print("{0: <15}".format(s),end='')
                        for row_index, label in enumerate(labels):
                            display_with_padding(label)
                            for column in data_pesanan:
                                display_with_padding(column[row_index])
                            print()
                        tambah_kamar_lagi2 = str(input("Apakah anda ingin menambah kamar lagi?: "))
                        while True:
                            if tambah_kamar_lagi2 == "Ya":
                                masukan_jenis_kamar2 = str(input("Masukkan jenis kamar yang diinginkan: "))
                                masukan_jumlah_kamar2 = int(input("Masukkan Jumlah Kamar: "))
                                masukan_jumlah_malam2 = int(input("Masukkan Jumlah Malam: "))
                                if masukan_jenis_kamar2 == "Deluxe":
                                    total_harga = data_kamar[3][3] * masukan_jumlah_kamar2 * masukan_jumlah_malam2
                                elif masukan_jenis_kamar == "Suite":
                                    total_harga = data_kamar[3][4] * masukan_jumlah_kamar2 * masukan_jumlah_malam2
                                elif masukan_jenis_kamar == "Presidential":
                                    total_harga = data_kamar[3][5] * masukan_jumlah_kamar2 * masukan_jumlah_malam2
                                else:
                                    pass
                                data_input_pesanan2 = [data_pesanan[0][2]+1, masukan_jenis_kamar2, masukan_jumlah_kamar2, masukan_jumlah_malam2, total_harga]
                                data_pesanan[0].append(data_input_pesanan2[0])
                                data_pesanan[1].append(data_input_pesanan2[1])
                                data_pesanan[2].append(data_input_pesanan2[2])
                                data_pesanan[3].append(data_input_pesanan2[3])
                                data_pesanan[4].append(data_input_pesanan2[4])
                                data_pesanan
                                labels = ['','','','','']
                                def display_with_padding(s):
                                    print("{0: <15}".format(s),end='')
                                for row_index, label in enumerate(labels):
                                    display_with_padding(label)
                                    for column in data_pesanan:
                                        display_with_padding(column[row_index])
                                    print()
                                tambah_kamar_lagi3 = str(input("Apakah anda ingin menambah kamar lagi?: "))
                                while True:
                                    if tambah_kamar_lagi3 == "Ya":
                                        masukan_jenis_kamar3 = str(input("Masukkan jenis kamar yang diinginkan: "))
                                        masukan_jumlah_kamar3 = int(input("Masukkan Jumlah Kamar: "))
                                        masukan_jumlah_malam3 = int(input("Masukkan Jumlah Malam: "))
                                        if masukan_jenis_kamar3 == "Suite":
                                            total_harga = data_kamar[3][4] * masukan_jumlah_kamar3 * masukan_jumlah_malam3
                                        elif masukan_jenis_kamar == "Presidential":
                                            total_harga = data_kamar[3][5] * masukan_jumlah_kamar3 * masukan_jumlah_malam3
                                        else:
                                            pass
                                        data_input_pesanan3 = [data_pesanan[0][2]+1, masukan_jenis_kamar3, masukan_jumlah_kamar3, masukan_jumlah_malam3, total_harga]
                                        data_pesanan[0].append(data_input_pesanan3[0])
                                        data_pesanan[1].append(data_input_pesanan3[1])
                                        data_pesanan[2].append(data_input_pesanan3[2])
                                        data_pesanan[3].append(data_input_pesanan3[3])
                                        data_pesanan[4].append(data_input_pesanan3[4])
                                        data_pesanan
                                        labels = ['','','','','','']
                                        def display_with_padding(s):
                                            print("{0: <15}".format(s),end='')
                                        for row_index, label in enumerate(labels):
                                            display_with_padding(label)
                                            for column in data_pesanan:
                                                display_with_padding(column[row_index])
                                            print()
                                        tambah_kamar_lagi4 = str(input("Apakah anda ingin menambah kamar lagi?: "))
                                        while True:
                                            if tambah_kamar_lagi4 == "Ya":
                                                masukan_jenis_kamar4 = str(input("Masukkan jenis kamar yang diinginkan: "))
                                                masukan_jumlah_kamar4 = int(input("Masukkan Jumlah Kamar: "))
                                                masukan_jumlah_malam4 = int(input("Masukkan Jumlah Malam: "))
                                                if masukan_jenis_kamar4 == "Presidential":
                                                    total_harga = data_kamar[3][5] * masukan_jumlah_kamar4 * masukan_jumlah_malam4
                                                else:
                                                    pass
                                                data_input_pesanan4 = [data_pesanan[0][2]+1, masukan_jenis_kamar4, masukan_jumlah_kamar4, masukan_jumlah_malam4, total_harga]
                                                data_pesanan[0].append(data_input_pesanan4[0])
                                                data_pesanan[1].append(data_input_pesanan4[1])
                                                data_pesanan[2].append(data_input_pesanan4[2])
                                                data_pesanan[3].append(data_input_pesanan4[3])
                                                data_pesanan[4].append(data_input_pesanan4[4])
                                                data_pesanan
                                                labels = ['','','','','','','']
                                                def display_with_padding(s):
                                                    print("{0: <15}".format(s),end='')
                                                for row_index, label in enumerate(labels):
                                                    display_with_padding(label)
                                                    for column in data_pesanan:
                                                        display_with_padding(column[row_index])
                                                    print()
                                                    mainmenu()
                                            else:
                                                save_data = str(input("Apakah anda ingin menyimpan data?: "))
                                                if save_data == "Ya":
                                                    print("Saving data...")
                                                    print("Data Successfully Saved!")
                                                    mainmenu()
                                                elif save_data == "Tidak":
                                                    mainmenu()
                                    else:
                                        save_data = str(input("Apakah anda ingin menyimpan data?: "))
                                        if save_data == "Ya":
                                            print("Saving data...")
                                            print("Data Successfully Saved!")
                                            mainmenu()
                                        elif save_data == "Tidak":
                                            mainmenu()
                            else:
                                save_data = str(input("Apakah anda ingin menyimpan data?: "))
                                if save_data == "Ya":
                                    print("Saving data...")
                                    print("Data Successfully Saved!")
                                    mainmenu()
                                elif save_data == "Tidak":
                                    mainmenu()
                    else:
                        save_data = str(input("Apakah anda ingin menyimpan data?: "))
                        if save_data == "Ya":
                            print("Saving data...")
                            print("Data Successfully Saved!")
                            mainmenu()
                        elif save_data == "Tidak":
                            mainmenu()
            else:
                mainmenu()

def ubahpesanan():
    while True:
        print(data_pesanan)
        print("1. Ubah pesanan")
        print("2. Keluar")
        menu2 = int(input("Masukkan angka Menu yang ingin dijalankan: "))
        if menu2 == 2:
            exit
        elif menu2 == 1:
            data_pesanan
            print("1. Jumlah Kamar Standard")
            print("2. Jumlah Kamar Superior")
            print("3. Jumlah Kamar Deluxe")
            print("4. Jumlah Kamar Suite")
            print("5. Jumlah Kamar Presidential")
            print("6. Jumlah Malam di Kamar Standard")
            print("7. Jumlah Malam di Kamar Superior")
            print("8. Jumlah Malam di Kamar Deluxe")
            print("9. Jumlah Malam di Kamar Suite")
            print("10. Jumlah Malam di Kamar Presidential")
            print("11. Selesai. Kembali ke Menu Utama.")
            while True:
                item_ubahan = int(input("Apa yang Hendak Diubah? Jika tidak ada, ketik 11"))
                if item_ubahan == 1:
                    item_ubahan_jumlah_kamar1 = int(input("Masukkan jumlah kamar Standard baru: "))
                    data_pesanan[2][2] = item_ubahan_jumlah_kamar1
                    total1 = data_kamar[3][1] * data_pesanan[2][2] * data_pesanan[3][2]
                    data_pesanan[4][2] = total1
                    data_pesanan
                elif item_ubahan == 2:
                    item_ubahan_jumlah_kamar2 = int(input("Masukkan jumlah kamar Superior baru: "))
                    data_pesanan[2][3] = item_ubahan_jumlah_kamar2
                    total2 = data_kamar[3][2] * data_pesanan[2][3] * data_pesanan[3][3]
                    data_pesanan[4][3] = total2
                    data_pesanan
                elif item_ubahan == 3:
                    item_ubahan_jumlah_kamar3 = int(input("Masukkan jumlah kamar Deluxe baru: "))
                    data_pesanan[2][4] = item_ubahan_jumlah_kamar3
                    total3 = data_kamar[3][3] * data_pesanan[2][4] * data_pesanan[3][4]
                    data_pesanan[4][4] = total3
                    data_pesanan
                elif item_ubahan == 4:
                    item_ubahan_jumlah_kamar4 = int(input("Masukkan jumlah kamar Suite baru: "))
                    data_pesanan[2][5] = item_ubahan_jumlah_kamar4
                    total4 = data_kamar[3][4] * data_pesanan[2][5] * data_pesanan[3][5]
                    data_pesanan[4][5] = total4
                    data_pesanan
                elif item_ubahan == 5:
                    item_ubahan_jumlah_kamar5 = int(input("Masukkan jumlah kamar Presidential baru: "))
                    data_pesanan[2][6] = item_ubahan_jumlah_kamar5
                    total5 = data_kamar[3][5] * data_pesanan[2][6] * data_pesanan[3][6]
                    data_pesanan[4][6] = total5
                    data_pesanan
                elif item_ubahan == 6:
                    item_ubahan_jumlah_malam1 = int(input("Masukkan jumlah malam baru di kamar Standard: "))
                    data_pesanan[3][2] = item_ubahan_jumlah_malam1
                    total6 = data_kamar[3][1] * data_pesanan[2][2] * data_pesanan[3][2]
                    data_pesanan[4][2] = total6
                    data_pesanan
                elif item_ubahan == 7:
                    item_ubahan_jumlah_malam2 = int(input("Masukkan jumlah malam baru di kamar Superior: "))
                    data_pesanan[3][3] = item_ubahan_jumlah_malam2
                    total7 = data_kamar[3][2] * data_pesanan[2][3] * data_pesanan[3][3]
                    data_pesanan[4][3] = total7
                    data_pesanan
                elif item_ubahan == 8:
                    item_ubahan_jumlah_malam3 = int(input("Masukkan jumlah kamar Deluxe baru: "))
                    data_pesanan[3][4] = item_ubahan_jumlah_malam3
                    total8 = data_kamar[3][3] * data_pesanan[2][4] * data_pesanan[3][4]
                    data_pesanan[4][4] = total8
                    data_pesanan
                elif item_ubahan == 9:
                    item_ubahan_jumlah_malam4 = int(input("Masukkan jumlah kamar Suite baru: "))
                    data_pesanan[3][5] = item_ubahan_jumlah_malam4
                    total9 = data_kamar[3][4] * data_pesanan[2][5] * data_pesanan[3][5]
                    data_pesanan[4][5] = total9
                    data_pesanan
                elif item_ubahan == 10:
                    item_ubahan_jumlah_kamar5 = int(input("Masukkan jumlah kamar Presidential baru: "))
                    data_pesanan[3][6] = item_ubahan_jumlah_kamar5
                    total10 = data_kamar[3][5] * data_pesanan[2][6] * data_pesanan[3][6]
                    data_pesanan[4][6] = total10
                    data_pesanan
                else:
                    mainmenu()
        mainmenu()

def hapuspesanan():
    while True:
        print(data_pesanan)
        masukan_angka3 = int(input("Masukkan index jenis kamar yang ingin dihapus: "))
        if masukan_angka3 == 1:
            data_pesanan[0].pop(2)
            data_pesanan[1].pop(2)
            data_pesanan[2].pop(2)
            data_pesanan[3].pop(2)
            data_pesanan[4].pop(2)
        elif masukan_angka3 == 2:
            data_pesanan[0].pop(3)
            data_pesanan[1].pop(3)
            data_pesanan[2].pop(3)
            data_pesanan[3].pop(3)
            data_pesanan[4].pop(3)
        elif masukan_angka3 == 3:
            data_pesanan[0].pop(4)
            data_pesanan[1].pop(4)
            data_pesanan[2].pop(4)
            data_pesanan[3].pop(4)
            data_pesanan[4].pop(4)
        elif masukan_angka3 == 4:
            data_pesanan[0].pop(5)
            data_pesanan[1].pop(5)
            data_pesanan[2].pop(5)
            data_pesanan[3].pop(5)
            data_pesanan[4].pop(5)
        elif masukan_angka3 == 5:
            data_pesanan[0].pop(6)
            data_pesanan[1].pop(6)
            data_pesanan[2].pop(6)
            data_pesanan[3].pop(6)
            data_pesanan[4].pop(6)
        else: 
            mainmenu()
        mainmenu()

def lihatpesanan():
        while True:
            print(data_pesanan)
            nanya = str(input("Kembali ke menu utama?"))
            if nanya == "Ya":
                mainmenu()
            else:
                pass

def pembayaran():
    data_pesanan
    total3 = 0
    if data_pesanan[4][3] != None:
        print("Total yang harus dibayar adalah: ", data_pesanan[4][2]+data_pesanan[4][3])
        total3 = data_pesanan[4][2]+data_pesanan[4][3]
    elif data_pesanan[4][3] != None and data_pesanan[4][4] != None:
        print("Total yang harus dibayar adalah: ", data_pesanan[4][2]+data_pesanan[4][3]+data_pesanan[4][4])
        total3 = data_pesanan[4][2]+data_pesanan[4][3]+data_pesanan[4][4]
    elif data_pesanan[4][3] != None and data_pesanan[4][4] != None and data_pesanan[4][5] != None:
        print("Total yang harus dibayar adalah: ", data_pesanan[4][2]+data_pesanan[4][3]+data_pesanan[4][4]+data_pesanan[4][5])
        total3 = data_pesanan[4][2]+data_pesanan[4][3]+data_pesanan[4][4]+data_pesanan[4][5]
    elif data_pesanan[4][3] != None and data_pesanan[4][4] != None and data_pesanan[4][5] != None and data_pesanan [4][6] != None:
        print("Total yang harus dibayar adalah: ", data_pesanan[4][2]+data_pesanan[4][3]+data_pesanan[4][4]+data_pesanan[4][5]+data_pesanan[4][6])
        total3 = data_pesanan[4][2]+data_pesanan[4][3]+data_pesanan[4][4]+data_pesanan[4][5]+data_pesanan[4][6]
    
    uang = int(input("Masukkan jumlah uang: "))
    while uang < total3:
        print("Uang anda kurang sebesar: ", total3-uang)
        uang = int(input("Masukkan jumlah uang: "))
    while uang >= total3:
        print(f"Terima kasih"'\n'"Uang kembali anda: ", uang-total3, "IDR")
        print("Terima kasih untuk telah bermalam di Hotel Purwadhika. Sampai jumpa kembali.")
        break
    mainmenu()


def mainmenu():
    while True:
        menu()
        masukan_angka = str(input("Masukkan angka Menu yang ingin dijalankan: "))
        if masukan_angka == "7":
            break
        elif masukan_angka == "1":
            tentanghotel()
        elif masukan_angka == "2":
            pesankamar()
        elif masukan_angka == "3":
            ubahpesanan()
        elif masukan_angka == "4":
            hapuspesanan()
        elif masukan_angka == "5":
            lihatpesanan()
        elif masukan_angka == "6":
            pembayaran()
        else:
            print("Data you entered is not valid. Please enter again.")
mainmenu()








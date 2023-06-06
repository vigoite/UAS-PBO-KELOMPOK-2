import random #Mengimpor modul random yang digunakan untuk menghasilkan nilai acak.
import string #Mengimpor modul string yang berisi fungsi-fungsi terkait pemrosesan string.
import PySimpleGUI as sg #Mengimpor library PySimpleGUI dan memberikan alias sg untuk mempermudah penggunaannya.

class PasswordGenerator: #Mendefinisikan Kelas PasswordGenerator.
    def __init__(self): #Mendefinisikan method __init__ yang akan dieksekusi saat objek kelas PasswordGenerator dibuat. 
        self.window = sg.Window("Pembuatan Password", self.tampilan(), size=(500, 250), background_color=("black")) #Membuat objek window PySimpleGUI dengan judul "Pembuatan Password", menggunakan tampilan yang diberikan oleh metode tampilan(), ukuran jendela sebesar (500, 250), dan background berwarna hitam.

    def run(self): #Mendefinisikan method run yang akan menjalankan program utama.
        while True: #Loop yang berjalan selama kondisi ini benar.
            event, values = self.window.read() #Membaca input dan kejadian (event) dari pengguna saat berinteraksi dengan jendela antarmuka.
            if event == "Keluar" or event == sg.WINDOW_CLOSED: #Memeriksa apakah pengguna menutup jendela atau memilih opsi "Keluar". Jika ya, maka loop dihentikan.
                break #menghentikan perulangan
            elif event == "Buat Password": #Memeriksa apakah pengguna memilih opsi "Buat Password". Jika ya, maka dilanjutkan dengan pembuatan password.
                panjang_input = values["PANJANG"] #Mengambil nilai input pengguna untuk panjang password dari elemen dengan kunci "PANJANG" dalam values.
                kombinasi = { #Membuat dictionary kombinasi yang berisi pilihan user untuk karakter yang akan digunakan dalam password (kapital, kecil, angka, simbol).
                    "kapital": values["kapital"], 
                    "kecil": values["kecil"], 
                    "angka": values["angka"], 
                    "simbol": values["simbol"] 
                }

                if not panjang_input: #Memeriksa apakah variabel panjang_input kosong atau tidak memiliki nilai (None). Jika ya, berarti pengguna tidak memasukkan panjang password.
                    sg.popup_ok("Harap masukkan panjang password!", button_color=("white", "green"), text_color=("black"), background_color=("lightblue")) #Menampilkan popup pesan dengan teks "Harap masukkan panjang password!" menggunakan fungsi sg.popup_ok() dari PySimpleGUI. Popup ini memberikan peringatan kepada pengguna bahwa panjang password harus diisi.
                    continue #Melanjutkan ke iterasi berikutnya dalam loop while. 
                try: #Memulai blok try-except untuk menangani pengecualian.
                    panjang = int(panjang_input) #Mengonversi panjang_input menjadi bilangan bulat (integer) menggunakan fungsi int(). Jika panjang_input tidak dapat diubah menjadi bilangan bulat, akan terjadi pengecualian ValueError.
                except ValueError: #Menangkap pengecualian ValueError yang terjadi jika panjang_input tidak dapat diubah menjadi bilangan bulat.
                    sg.popup_ok("Karakter yang dimasukkan tidak valid!", button_color=("white", "green"), text_color=("black"), background_color=("lightblue")) #Menampilkan popup pesan dengan teks "Karakter yang dimasukkan tidak valid!" menggunakan fungsi sg.popup_ok(). Popup ini memberikan peringatan kepada pengguna bahwa karakter yang dimasukkan tidak valid.
                    continue #Melanjutkan ke iterasi berikutnya dalam loop while
                password = self.generate_password(panjang, kombinasi) #Memanggil metode generate_password() dari objek self (kelas PasswordGenerator) dengan argumen panjang dan kombinasi. Metode ini akan menghasilkan password acak berdasarkan panjang dan pilihan karakter yang diberikan.
                if password: # Memeriksa apakah password berhasil dihasilkan (tidak bernilai None atau False).
                    self.window["PASSWORD"].update(password) #Menggunakan metode update() pada elemen dengan kunci "PASSWORD" pada jendela antarmuka untuk memperbarui teks dengan nilai password yang dihasilkan.

        self.window.close() #Menutup jendela setelah loop selesai.

    def tampilan(self): #Mendefinisikan metode tampilan()
        return [ # Mengembalikan daftar (list) berisi elemen-elemen.
            [sg.Text("Panjang Password :", text_color=("white"), background_color=("black")), sg.Input(key="PANJANG",pad=((10, 10), (10, 10)))], #Menambahkan elemen teks dengan teks "Panjang Password :" dengan teks berwarna putih dan latar belakang hitam, diikuti dengan elemen input yang digunakan untuk memasukkan panjang password. Elemen input memiliki kunci (key) "PANJANG" yang digunakan untuk mengakses nilai yang dimasukkan oleh pengguna. pad=((10, 10), (10, 10)) mengatur padding (jarak) dari elemen tersebut.
            [sg.Checkbox("Huruf Kapital", key="kapital", text_color=("white"), background_color=("black")), sg.Checkbox("Huruf Kecil", key="kecil", text_color=("white"), background_color=("black"), pad=((15, 10), (10, 10)))], #Menambahkan dua elemen checkbox untuk memilih huruf kapital dan huruf kecil. 
            [sg.Checkbox("Angka", key="angka", text_color=("white"), background_color=("black")), sg.Checkbox("Simbol", key="simbol", text_color=("white"), background_color=("black"), pad=((52, 10), (10, 10))),sg.Button("Buat Password", button_color=("white", "darkblue"), pad=((160, 10), (0, 10)))], #Menambahkan dua elemen checkbox untuk memilih angka dan simbol.
            [sg.Text("Password :", text_color=("white"), background_color=("black")), sg.Input(key="PASSWORD", disabled=True, pad=((60, 10), (10, 10)))], #Menambahkan elemen teks dengan teks "Password :", diikuti dengan elemen input yang digunakan untuk menampilkan password yang dihasilkan. 
            [sg.Button("Keluar", button_color=("white", "red"), pad=((413, 10), (10, 10)))], #enambahkan elemen tombol "Keluar" dengan teks berwarna putih dan latar belakang merah.
        ]

    def generate_password(self, panjang, kombinasi): #endefinisikan metode generate_password()
        if panjang < 10: #Memeriksa apakah panjang password yang dimasukkan lebih kecil dari 8 karakter.
            sg.popup_ok("Panjang password minimal 10 karakter!", button_color=("white", "green"), text_color=("black"), background_color=("lightblue")) #Menampilkan popup pesan dengan teks "Panjang password minimal 8 karakter!" menggunakan fungsi sg.popup_ok() dari PySimpleGUI.
            return #Menghentikan eksekusi metode generate_password() dan mengembalikan None.
        
        if panjang > 25: #Memeriksa apakah panjang password yang dimasukkan lebih besar dari 20 karakter.
            sg.popup_ok("Panjang password maksimal 25 karakter!", button_color=("white", "green"), text_color=("black"), background_color=("lightblue")) #Menampilkan popup pesan dengan teks "Panjang password maksimal 20 karakter!" menggunakan fungsi sg.popup_ok().
            return #Menghentikan eksekusi metode generate_password() dan mengembalikan None.

        kombinasi_terpilih = [] #Membuat list kosong dengan nama kombinasi_terpilih yang akan digunakan untuk menyimpan kombinasi karakter yang dipilih.
        if kombinasi["kapital"]: #Memeriksa apakah pengguna memilih opsi "Huruf Kapital" (kombinasi["kapital"] bernilai True).
            kombinasi_terpilih.append(string.ascii_uppercase) #Jika opsi "Huruf Kapital" dipilih, maka string.ascii_uppercase (string yang berisi huruf kapital A-Z) akan ditambahkan ke kombinasi_terpilih.
        if kombinasi["kecil"]: # Memeriksa apakah pengguna memilih opsi "Huruf Kecil" (kombinasi["kecil"] bernilai True).
            kombinasi_terpilih.append(string.ascii_lowercase) #Jika opsi "Huruf Kecil" dipilih, maka string.ascii_lowercase (string yang berisi huruf kecil a-z) akan ditambahkan ke kombinasi_terpilih.
        if kombinasi["angka"]: #Memeriksa apakah pengguna memilih opsi "Angka" (kombinasi["angka"] bernilai True).
            kombinasi_terpilih.append(string.digits) #Jika opsi "Angka" dipilih, maka string.digits (string yang berisi angka 0-9) akan ditambahkan ke kombinasi_terpilih.
        if kombinasi["simbol"]: #Memeriksa apakah pengguna memilih opsi "Simbol" (kombinasi["simbol"] bernilai True).
            kombinasi_terpilih.append(string.punctuation) #Jika opsi "Simbol" dipilih, maka string.punctuation (string yang berisi simbol-simbol) akan ditambahkan ke kombinasi_terpilih.

        if not kombinasi_terpilih: #Memeriksa apakah kombinasi_terpilih kosong, yaitu tidak ada kombinasi karakter yang dipilih.
            sg.popup_ok("Harap pilih minimal satu kombinasi karakter!", button_color=("white", "green"), text_color=("black"), background_color=("lightblue")) #Menampilkan popup pesan dengan teks "Harap pilih minimal satu kombinasi karakter!" menggunakan fungsi sg.popup_ok(). 
            return #Menghentikan eksekusi metode generate_password() dan mengembalikan None.

        password = [] #Membuat list kosong dengan nama password yang akan digunakan untuk menyimpan karakter-karakter yang akan membentuk password.
        for _ in range(panjang): #Melakukan perulangan sebanyak panjang kali, di mana setiap iterasi akan menambahkan satu karakter ke dalam password.
            char_pool = random.choice(kombinasi_terpilih) #Memilih secara acak salah satu kombinasi karakter yang telah dipilih sebelumnya dari kombinasi_terpilih menggunakan fungsi random.choice(). 
            password.append(random.choice(char_pool)) #Memilih secara acak satu karakter dari char_pool menggunakan fungsi random.choice() dan menambahkannya ke dalam password.

        random.shuffle(password) #Mengacak urutan karakter dalam password menggunakan fungsi random.shuffle(). 
        password = ''.join(password) #Menggabungkan semua karakter dalam password menjadi sebuah string menggunakan metode ''.join() dengan delimiter string kosong.
        return password #Mengembalikan password yang dihasilkan.

if __name__ == "__main__": #Memeriksa apakah file ini dieksekusi sebagai skrip utama.
    generator = PasswordGenerator() #Membuat objek PasswordGenerator dengan menyimpannya ke dalam variabel generator.
    generator.run() #Memanggil metode run() dari objek generator untuk menjalankan aplikasi GUI pembuatan password.

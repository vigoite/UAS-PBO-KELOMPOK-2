# UAS-PBO-KELOMPOK-2

Anggota Kelompok :
Beny Esa Pratama (G1A022013)
Riolan Pratama (G1A022047)
Vigo Ite Anugrahesa (G1A022089)

Penjelasan program :
1.	Class PasswordGenerator Ini adalah kelas utama yang digunakan untuk mengatur pembuatan password.
2.	Metode __init__(self) adalah konstruktor yang digunakan untuk inisialisasi objek kelas PasswordGenerator dan membuat jendela GUI menggunakan modul PySimpleGUI.
3.	Metode run(self) adalah metode utama yang digunakan untuk menjalankan program. Metode ini berisi loop while yang terus berjalan sampai pengguna menutup jendela atau memilih opsi "Keluar".
4.	Metode tampilan(self) digunakan untuk mengatur tampilan GUI jendela dengan menggunakan PySimpleGUI. Metode ini mengembalikan daftar elemen-elemen GUI yang akan ditampilkan.
5.	Metode generate_password(self, panjang, kombinasi) digunakan untuk menghasilkan password berdasarkan panjang yang dimasukkan oleh pengguna dan pilihan kombinasi karakter. Metode ini mengembalikan password yang dihasilkan.
6.	Metode __name__ == "__main__" adalah blok kode yang akan dieksekusi jika skrip ini dijalankan sebagai skrip utama. Membuat objek PasswordGenerator dan menjalankan metode run() untuk memulai program.

Selain itu, terdapat penggunaan konsep OOP berikut dalam program:
1.	Encapsulation: Variabel self.window bersifat private karena diawali dengan underscore _, sehingga hanya dapat diakses di dalam class PasswordGenerator.
2.	Inheritance: Class PasswordGenerator tidak mewarisi dari class lain, tetapi bisa saja mewarisi dari class lain jika ada kebutuhan di masa depan.
3.	Abstraction: Class PasswordGenerator mengabstraksi konsep pembuatan dan pengelolaan password. Pengguna program tidak perlu tahu bagaimana password dibuat atau dikelola, hanya perlu memasukkan panjang password dan memilih kombinasi karakter.

# Pertemuan 07 Fungsi Python

Nama: Ahadin Ilman
NIM: [Isi NIM Anda]
Kelas: [Isi Kelas Anda]

## Tujuan
Menggunakan fungsi, parameter, return value, dan scope untuk membuat program modular.

## Cara Menjalankan
python3 praktik/utilitas_matematika.py

## Struktur Fungsi
- `luas_persegi_panjang(p, l)`: Menerima parameter p (panjang) dan l (lebar), mengembalikan nilai luas.
- `luas_segitiga(a, t)`: Menerima parameter a (alas) dan t (tinggi), mengembalikan nilai luas.
- `jumlah_n(n)`: Menerima parameter n, mengembalikan jumlah deret 1 hingga n.
- `faktorial(n)`: Menerima parameter n, mengembalikan hasil perkalian faktorial n!.
- `tampilkan_menu()`: Menampilkan opsi operasi matematika ke layar.

## Hasil Pengujian
| Operasi | Input | Hasil Diharapkan | Hasil Aktual | Status |
|---|---|---|---|---|
| Luas persegi panjang | p=8, l=5 | 40 | 40 | Sesuai |
| Luas segitiga | a=10, t=6 | 30.0 | 30.0 | Sesuai |
| Jumlah 1..n | n=10 | 55 | 55 | Sesuai |
| Faktorial | n=5 | 120 | 120 | Sesuai |
| Faktorial | n=0 | 1 | 1 | Sesuai |

## Refleksi
Penggunaan fungsi memisahkan logika perhitungan dari antarmuka menu program. Kode menjadi lebih rapi, tidak terjadi pengulangan rumus, dan pemecahan masalah (debugging) menjadi lebih mudah.
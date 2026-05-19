Tugas akhir percobaan 3

Judul : Program Sistem Antrian Menggunakan Queue Array

Program ini dibuat buat ngatur antrian sederhana pakai struktur data queue dan array. Jadi cara kerjanya mirip banget kayak antrian di bank, rumah sakit, atau kantin, siapa yang masuk duluan bakal dipanggil duluan juga. Di program ini user bisa nambah nomor antrian, manggil antrian paling depan, ngecek siapa yang lagi di depan, sama lihat semua isi antrian yang ada. Program juga bakal ngecek apakah antrian masih kosong atau malah udah penuh, jadi lebih aman pas dipakai dan nggak bikin error.


Source Code:

<img width="1564" height="3800" alt="carbon queue array" src="https://github.com/user-attachments/assets/11262598-4504-428f-a904-4a0d051a06c2" />

1. Mendefinisikan class QueueArray untuk membuat struktur data antrian.
2. Constructor untuk menginisialisasi object queue dengan ukuran maksimum 100.
3. Menyimpan ukuran maksimum queue ke variabel MAXN.
4. Membuat array kosong berisi None sesuai ukuran maksimum queue.
5. Mengatur indeks depan queue menjadi -1 sebagai tanda queue kosong.
6. Mengatur indeks belakang queue menjadi -1.
7. Kosong.
8. Mendefinisikan fungsi untuk mengecek apakah queue kosong.
9. Mengembalikan nilai True jika queue kosong.
10. Kosong.
11. Mendefinisikan fungsi untuk mengecek apakah queue penuh.
12. Mengecek apakah posisi belakang berikutnya sama dengan posisi depan.
13. Kosong.
14. Mendefinisikan fungsi untuk menambahkan data ke queue.
15. Mengecek apakah queue penuh.
16. Menampilkan pesan bahwa antrian penuh.
17. Menghentikan fungsi jika queue penuh.
18. Mengecek apakah queue kosong.
19. Mengatur indeks depan menjadi 0 saat data pertama masuk.
20. Mengatur indeks belakang menjadi 0.
21. Jika queue tidak kosong.
22. Menggeser indeks belakang ke posisi berikutnya secara circular.
23. Menyimpan data ke posisi belakang queue.
24. Menampilkan pesan bahwa nomor antrian berhasil ditambahkan.
25. Kosong.
26. Mendefinisikan fungsi untuk memanggil atau menghapus data dari queue.
27. Mengecek apakah queue kosong.
28. Menampilkan pesan bahwa antrian kosong.
29. Menghentikan fungsi jika queue kosong.
30. Menampilkan nomor antrian yang dipanggil.
31. Mengecek apakah queue hanya memiliki satu data.
32. Mengosongkan indeks depan queue.
33. Mengosongkan indeks belakang queue.
34. Jika queue masih memiliki data lain.
35. Menggeser indeks depan ke data berikutnya secara circular.
36. Kosong.
37. Mendefinisikan fungsi untuk melihat data paling depan queue tanpa menghapusnya.
38. Mengecek apakah queue kosong.
39. Menampilkan pesan bahwa antrian kosong.
40. Menghentikan fungsi jika queue kosong.
41. Menampilkan data paling depan pada queue.
42. Kosong.
43. Mendefinisikan fungsi untuk menampilkan seluruh isi queue.
44. Mengecek apakah queue kosong.
45. Menampilkan pesan bahwa antrian kosong.
46. Menghentikan fungsi jika queue kosong.
47. Menampilkan tulisan daftar antrian.
48. Menyimpan indeks depan queue ke variabel i.
49. Melakukan perulangan untuk menampilkan seluruh isi queue.
50. Menampilkan isi queue pada indeks i.
51. Mengecek apakah sudah mencapai indeks belakang.
52. Menghentikan perulangan.
53. Menggeser indeks ke posisi berikutnya secara circular.
54. Membuat pindah baris setelah queue ditampilkan.
55. Kosong.
56. Kosong.
57. Mendefinisikan fungsi utama program.
58. Membuat object queue dari class QueueArray.
59. Menginisialisasi variabel pilihan menu dengan nilai 0.
60. Melakukan perulangan selama pilihan bukan 5.
61. Menampilkan judul menu program.
62. Menampilkan menu tambah antrian.
63. Menampilkan menu panggil antrian.
64. Menampilkan menu lihat antrian depan.
65. Menampilkan menu tampilkan semua antrian.
66. Menampilkan menu keluar program.
67. Blok percobaan untuk menangani error input.
68. Meminta pengguna memasukkan pilihan menu.
69. Menangani error jika input bukan angka.
70. Menampilkan pesan input tidak valid.
71. Mengulang kembali ke awal perulangan.
72. Kosong.
73. Mengecek apakah pengguna memilih menu 1.
74. Blok percobaan untuk input nomor antrian.
75. Meminta pengguna memasukkan nomor antrian.
76. Menambahkan nomor antrian ke queue.
77. Menangani error jika input bukan angka.
78. Menampilkan pesan input tidak valid.
79. Mengecek apakah pengguna memilih menu 2.
80. Memanggil atau menghapus antrian terdepan.
81. Mengecek apakah pengguna memilih menu 3.
82. Menampilkan antrian terdepan tanpa menghapusnya.
83. Mengecek apakah pengguna memilih menu 4.
84. Menampilkan seluruh isi antrian.
85. Mengecek apakah pengguna memilih menu 5.
86. Menampilkan pesan program selesai.
87. Jika pilihan menu tidak tersedia.
88. Menampilkan pesan pilihan tidak valid.
89. Kosong.
90. Kosong.
91. Mengecek apakah file dijalankan sebagai program utama.
92. Memanggil fungsi main() untuk menjalankan program.


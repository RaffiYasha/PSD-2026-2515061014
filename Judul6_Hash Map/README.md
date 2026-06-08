Judul : Program Penyimpanan Data Kontak Menggunakan Hash Map Separate Chaining

Program ini dibuat untuk mengelola data kontak sederhana menggunakan struktur data Hash Map dengan metode Separate Chaining. Cara kerjanya mirip seperti buku kontak pada ponsel, di mana setiap kontak memiliki ID sebagai kunci (key) dan nama kontak sebagai nilai (value). Dengan menggunakan Hash Map, proses penyimpanan, pencarian, dan penghapusan data dapat dilakukan dengan cepat.

Source Code:

<img width="1462" height="3464" alt="carbon hash map" src="https://github.com/user-attachments/assets/7978ba3a-4d1e-472d-80cf-8f955e9009cc" />

1. Mendefinisikan class Node untuk menyimpan data pada linked list.
2. Constructor untuk menginisialisasi node baru.
3. Menyimpan key ke atribut key.
4. Menyimpan value ke atribut value.
5. Mengatur pointer next menjadi None.
6. Kosong.
7. Mendefinisikan class HashMapSeparateChaining.
8. Constructor untuk menginisialisasi Hash Map.
9. Menyimpan ukuran Hash Map ke variabel SIZE.
10. Membuat tabel Hash Map berisi nilai None sesuai ukuran yang ditentukan.
11. Kosong.
12. Mendefinisikan fungsi hash untuk menentukan indeks penyimpanan data.
13. Menghitung indeks menggunakan operasi modulo.
14. Kosong.
15. Mendefinisikan fungsi untuk menambahkan data ke Hash Map.
16. Menghitung indeks dari key yang diberikan.
17. Mengambil node pertama pada indeks tersebut.
18. Melakukan perulangan selama node masih ada.
19. Mengecek apakah key sudah ada.
20. Mengubah value jika key ditemukan.
21. Menghentikan fungsi.
22. Berpindah ke node berikutnya.
23. Membuat node baru.
24. Menghubungkan node baru ke awal linked list pada indeks tersebut.
25. Menjadikan node baru sebagai kepala linked list.
26. Kosong.
27. Mendefinisikan fungsi untuk mencari data berdasarkan key.
28. Menghitung indeks dari key yang dicari.
29. Mengambil node pertama pada indeks tersebut.
30. Melakukan perulangan selama node masih ada.
31. Mengecek apakah key ditemukan.
32. Mengembalikan node yang ditemukan.
33. Berpindah ke node berikutnya.
34. Mengembalikan nilai None jika data tidak ditemukan.
35. Kosong.
36. Mendefinisikan fungsi untuk menghapus data berdasarkan key.
37. Menghitung indeks dari key yang akan dihapus.
38. Mengambil node pertama pada indeks tersebut.
39. Membuat variabel prev untuk menyimpan node sebelumnya.
40. Melakukan perulangan selama node masih ada.
41. Mengecek apakah key ditemukan.
42. Mengecek apakah node yang dihapus berada di awal linked list.
43. Menggeser head ke node berikutnya.
44. Jika node bukan berada di awal linked list.
45. Menghubungkan node sebelumnya ke node setelah node yang dihapus.
46. Mengembalikan nilai True sebagai tanda data berhasil dihapus.
47. Memindahkan prev ke node saat ini.
48. Berpindah ke node berikutnya.
49. Mengembalikan nilai False jika data tidak ditemukan.
50. Kosong.
51. Mendefinisikan fungsi untuk menampilkan seluruh isi Hash Map.
52. Menampilkan judul daftar kontak.
53. Melakukan perulangan untuk setiap indeks tabel Hash Map.
54. Menampilkan nomor indeks.
55. Mengambil node pertama pada indeks tersebut.
56. Melakukan perulangan selama node masih ada.
57. Menampilkan key dan value pada node.
58. Berpindah ke node berikutnya.
59. Menampilkan NULL sebagai penanda akhir linked list.
60. Kosong.
61. Mendefinisikan fungsi utama program.
62. Membuat objek Hash Map bernama kontak.
63. Kosong.
64. Menambahkan kontak dengan ID 1 dan nama Andi.
65. Menambahkan kontak dengan ID 11 dan nama Budi.
66. Menambahkan kontak dengan ID 21 dan nama Cici.
67. Menambahkan kontak dengan ID 2 dan nama Dodi.
68. Kosong.
69. Menampilkan seluruh data kontak.
70. Kosong.
71. Mencari kontak dengan ID 11.
72. Mengecek apakah kontak ditemukan.
73. Menampilkan nama kontak yang ditemukan.
74. Jika kontak tidak ditemukan.
75. Menampilkan pesan bahwa kontak tidak ditemukan.
76. Kosong.
77. Menghapus kontak dengan ID 11.
78. Kosong.
79. Menampilkan informasi setelah penghapusan kontak.
80. Menampilkan kembali seluruh isi Hash Map.
81. Kosong.
82. Mengecek apakah file dijalankan sebagai program utama.
83. Menjalankan fungsi main().

Output Code:

<img width="738" height="657" alt="Screenshot 2026-06-08 190831" src="https://github.com/user-attachments/assets/99c8839a-af3a-44de-a0fe-3374cddaff62" />


link YouTube:

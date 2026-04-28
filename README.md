
Tugas Akhir Percobaan 1

Judul : Sistem Skor Game per Ronde

Program ini berfungsi sebagai sistem menghiutng skor game yang dirancang untuk memudahkan pengguna dalam mencatat, melihat, dan mengubah skor pada setiap ronde secara terstruktur. Program menyediakan beberapa fitur utama seperti input skor untuk setiap ronde, pencarian skor berdasarkan ronde tertentu, serta pengubahan skor jika terjadi kesalahan input. Dengan adanya fitur tersebut, pengguna dapat mengelola data skor secara lebih efisien dan terorganisir.
Struktur data yang digunakan dalam program ini adalah List satu dimensi (1D), di mana setiap elemen dalam list merepresentasikan skor pada satu ronde permainan. 
      Index pada list dimulai dari 0, namun dalam implementasinya ditampilkan sebagai ronde 1 hingga 5 agar lebih mudah dipahami oleh pengguna. Program ini juga memanfaatkan perulangan (looping) untuk mengakses setiap elemen dalam list, serta menggunakan percabangan (if-else) untuk mengatur alur logika program berdasarkan pilihan menu yang dipilih oleh user.

source Code :


<img width="1598" height="3314" alt="carbon_tugas akhir judul 1" src="https://github.com/user-attachments/assets/dd861598-513b-46ea-89e8-cc5a90905d00" />



1. Mendefinisikan fungsi bernama menu untuk membungkus kode yang menampilkan daftar pilihan
2. Mencetak opsi pertama untuk menampilkan address list skor
3. Mencetak opsi kedua untuk menampilkan address setiap ronde
4. Mencetak opsi ketiga untuk memasukkan skor ke dalam list
5. Mencetak opsi keempat untuk mencari skor berdasarkan ronde
6. Mencetak opsi kelima untuk mengubah skor pada ronde tertentu
7. Mencetak opsi keenam untuk keluar dari program
8.
9.
10. Mendefinisikan fungsi utama main sebagai tempat seluruh logika program dijalankan
11. Membuat list a dengan 5 elemen bernilai awal 0 sebagai tempat menyimpan skor tiap ronde
12. Membuat variabel running bernilai True untuk mengontrol perulangan program
13. Memulai perulangan selama running bernilai True
14. Memanggil fungsi menu untuk menampilkan pilihan ke user
15. Memulai blok penanganan error menggunakan try-except
16. Mengambil input pilihan dari user dan mengubahnya menjadi integer
17. Menangkap error jika input bukan angka
18. Menampilkan pesan kesalahan jika terjadi error input
19. Melanjutkan perulangan ke menu awal jika terjadi error
20. 
21. Mengecek jika user memilih menu nomor 1
22. Menampilkan address list skor menggunakan fungsi id()
23.
24. Mengecek jika user memilih menu nomor 2
25. Melakukan perulangan dari index 0 sampai 4
26. Menampilkan address setiap elemen dalam list sebagai ronde 1 sampai 5
27.
28. Mengecek jika user memilih menu nomor 3
29. Menampilkan pesan untuk memasukkan skor setiap ronde
30. Melakukan perulangan sebanyak 5 kali untuk input skor
31. Memulai perulangan while True agar input valid
32. Memulai blok try untuk input skor
33. Mengambil input skor dari user dan menyimpannya ke dalam list
34. Keluar dari perulangan jika input valid
35. Menangkap error jika input bukan angka
36. Menampilkan pesan kesalahan dan meminta input ulang
37. Menampilkan isi list skor setelah semua data dimasukkan
38.
39. Mengecek jika user memilih menu nomor 4
40. Memulai blok try untuk mencari skor
41. Meminta user memasukkan nomor ronde (1-5)
42. Melakukan validasi apakah ronde berada dalam rentang yang benar
43. Menampilkan skor sesuai ronde dengan mengambil data dari list menggunakan r-1
44.
45. Menampilkan pesan jika ronde tidak valid
46. Menangkap error jika input tidak valid
47. Menampilkan pesan kesalahan input
48.
49. Mengecek jika user memilih menu nomor 5
50. Memulai blok try untuk mengubah skor
51. Meminta user memasukkan ronde yang ingin diubah
52. Melakukan validasi ronde
53. Meminta user memasukkan skor baru
54. Mengubah nilai dalam list pada posisi r-1
55. Menampilkan isi list setelah diperbarui
56.
57. Menampilkan pesan jika ronde tidak valid
58. Menangkap error jika input tidak valid
59. Menampilkan pesan kesalahan input
60.
61. Mengecek jika user memilih menu nomor 6
62. Mengubah nilai running menjadi False untuk menghentikan program
63. Menampilkan pesan bahwa program selesai
64.
65. Jika pilihan tidak sesuai menu
66. Menampilkan pesan bahwa pilihan tidak valid
67    
68.
69. Mengecek apakah file dijalankan secara langsung
70. Memanggil fungsi main untuk menjalankan program


Output Menu : 
<img width="293" height="101" alt="Screenshot 2026-04-28 204228" src="https://github.com/user-attachments/assets/5084b0d7-63e0-4ed6-b242-446693cc5ba6" />

Menu 1 : 
<img width="248" height="34" alt="Screenshot 2026-04-28 204237" src="https://github.com/user-attachments/assets/05e6f813-9feb-49ed-8eeb-15aad68d4df5" />

Menu 2 :
<img width="248" height="101" alt="Screenshot 2026-04-28 204247" src="https://github.com/user-attachments/assets/7eb27a1c-8169-4d3a-986f-92ea248e21dc" />

Menu 3 : 
<img width="274" height="137" alt="Screenshot 2026-04-28 204256" src="https://github.com/user-attachments/assets/bf6ec8d3-abd7-4afa-8154-dbf77acbed3f" />

Menu 4 : 
<img width="187" height="51" alt="Screenshot 2026-04-28 204308" src="https://github.com/user-attachments/assets/3e657e5e-0969-48fb-9ae3-ef52e8a88e26" />

Menu 5 : 
<img width="309" height="69" alt="Screenshot 2026-04-28 204320" src="https://github.com/user-attachments/assets/558e0167-afb6-405d-92a7-31da4b9827cd" />

Menu 6 :
<img width="135" height="30" alt="Screenshot 2026-04-28 204327" src="https://github.com/user-attachments/assets/70cb5d4e-fa42-4f95-827e-ca3125402ff0" />

Link YouTube : https://youtu.be/L2cyhfjpnts

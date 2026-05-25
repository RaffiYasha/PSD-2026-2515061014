
Tiugas Akhir Percobaan 5

Judul : Program Pengelolaan Data Harga Produk Menggunakan Binary Search Tree (BST)

Program ini dibuat buat ngatur data harga produk toko pakai struktur data Binary Search Tree (BST). Cara kerjanya mirip kayak nyusun data harga barang supaya lebih gampang dicari dan diurutkan. Di program ini user bisa nambah harga produk, cari harga tertentu, lihat daftar harga dari yang paling murah sampai paling mahal, serta ngecek harga termurah dan termahal. Selain itu program juga bisa ngitung jumlah produk dan total seluruh harga produk yang ada di dalam data. Jadi program ini cocok dipakai buat simulasi pengelolaan data produk sederhana biar pencarian dan pengurutan data jadi lebih cepat dan rapi.


Source code:

<img width="1648" height="6332" alt="carbon BST TA" src="https://github.com/user-attachments/assets/64f31bcd-3d87-4565-a2aa-75897cbcaf0f" />

1. Mendefinisikan class Node untuk membuat node pada struktur data Binary Search Tree (BST).
2. Constructor untuk menginisialisasi data node berupa harga produk.
3. Menyimpan nilai harga ke variabel key.
4. Mengatur child kiri (left) menjadi None.
5. Mengatur child kanan (right) menjadi None.
6. Kosong.
7. Mendefinisikan class BSTProduk untuk membuat struktur data Binary Search Tree data harga produk.
8. Constructor untuk menginisialisasi root BST.
9. Mengatur root tree menjadi None sebagai tanda BST masih kosong.
10. Kosong.
11. Mendefinisikan fungsi insert_node untuk menambahkan node baru ke BST secara rekursif.
12. Mengecek apakah root kosong.
13. Membuat node baru jika root kosong.
14. Mengecek apakah harga lebih kecil dari root.
15. Menambahkan data ke subtree kiri secara rekursif.
16. Mengecek apakah harga lebih besar dari root.
17. Menambahkan data ke subtree kanan secara rekursif.
18. Mengembalikan root setelah proses insert selesai.
19. Kosong.
20. Mendefinisikan fungsi insert untuk memanggil proses penambahan data ke BST.
21. Menambahkan data harga ke dalam BST melalui fungsi insert_node.
22. Kosong.
23. Mendefinisikan fungsi search_node untuk mencari data harga pada BST secara rekursif.
24. Mengecek apakah root kosong.
25. Mengembalikan nilai False jika data tidak ditemukan.
26. Mengecek apakah data pada root sama dengan harga yang dicari.
27. Mengembalikan nilai True jika data ditemukan.
28. Mengecek apakah harga lebih kecil dari root.
29. Melanjutkan pencarian ke subtree kiri secara rekursif.
30. Melanjutkan pencarian ke subtree kanan secara rekursif.
31. Kosong.
32. Mendefinisikan fungsi search untuk memanggil proses pencarian data pada BST.
33. Mengembalikan hasil pencarian dari fungsi search_node.
34. Kosong.
35. Mendefinisikan fungsi inorder untuk menampilkan data BST secara urut naik (ascending).
36. Mengecek apakah root kosong.
37. Menghentikan fungsi jika root kosong.
38. Menelusuri subtree kiri terlebih dahulu.
39. Menampilkan nilai root.
40. Menelusuri subtree kanan.
41. Kosong.
42. Mendefinisikan fungsi preorder untuk menampilkan data BST dengan metode preorder traversal.
43. Mengecek apakah root kosong.
44. Menghentikan fungsi jika root kosong.
45. Menampilkan nilai root terlebih dahulu.
46. Menelusuri subtree kiri.
47. Menelusuri subtree kanan.
48. Kosong.
49. Mendefinisikan fungsi postorder untuk menampilkan data BST dengan metode postorder traversal.
50. Mengecek apakah root kosong.
51. Menghentikan fungsi jika root kosong.
52. Menelusuri subtree kiri terlebih dahulu.
53. Menelusuri subtree kanan.
54. Menampilkan nilai root terakhir.
55. Kosong.
56. Mendefinisikan fungsi find_min untuk mencari harga paling rendah pada BST.
57. Mengecek apakah root kosong.
58. Mengembalikan nilai -1 jika BST kosong.
59. Menyimpan root ke variabel current.
60. Melakukan perulangan selama child kiri masih ada.
61. Menggeser posisi current ke node kiri.
62. Mengembalikan nilai terkecil dari BST.
63. Kosong.
64. Mendefinisikan fungsi find_max untuk mencari harga paling tinggi pada BST.
65. Mengecek apakah root kosong.
66. Mengembalikan nilai -1 jika BST kosong.
67. Menyimpan root ke variabel current.
68. Melakukan perulangan selama child kanan masih ada.
69. Menggeser posisi current ke node kanan.
70. Mengembalikan nilai terbesar dari BST.
71. Kosong.
72. Mendefinisikan fungsi count_nodes untuk menghitung jumlah seluruh node pada BST.
73. Mengecek apakah root kosong.
74. Mengembalikan nilai 0 jika BST kosong.
75. Menghitung jumlah node pada subtree kiri dan kanan secara rekursif lalu menjumlahkannya.
76. Kosong.
77. Mendefinisikan fungsi sum_nodes untuk menghitung total seluruh harga produk pada BST.
78. Mengecek apakah root kosong.
79. Mengembalikan nilai 0 jika BST kosong.
80. Menjumlahkan nilai root dengan subtree kiri dan subtree kanan secara rekursif.
81. Kosong.
82. Mendefinisikan fungsi utama program.
83. Membuat object BST dari class BSTProduk.
84. Menginisialisasi variabel pilihan menu dengan nilai 0.
85. Kosong.
86. Melakukan perulangan selama pilihan bukan 10.
87. Menampilkan judul menu program.
88. Menampilkan menu tambah harga produk.
89. Menampilkan menu cari harga produk.
90. Menampilkan menu tampilkan harga urut naik (Inorder).
91. Menampilkan menu tampilkan data preorder.
92. Menampilkan menu tampilkan data postorder.
93. Menampilkan menu harga termurah.
94. Menampilkan menu harga termahal.
95. Menampilkan menu jumlah produk.
96. Menampilkan menu total seluruh harga.
97. Menampilkan menu keluar program.
98. Kosong.
99. Blok percobaan untuk menangani error input menu.
100. Meminta pengguna memasukkan pilihan menu.
101. Menangani error jika input bukan angka.
102. Menampilkan pesan input tidak valid.
103. Mengulang kembali ke awal perulangan.
104. Kosong.
105. Mengecek apakah pengguna memilih menu 1.
106. Blok percobaan untuk input harga produk.
107. Meminta pengguna memasukkan harga produk.
108. Menambahkan harga produk ke BST.
109. Menampilkan pesan bahwa harga berhasil ditambahkan.
110. Menangani error jika input bukan angka.
111. Menampilkan pesan input tidak valid.
112. Kosong.
113. Mengecek apakah pengguna memilih menu 2.
114. Blok percobaan untuk pencarian harga produk.
115. Meminta pengguna memasukkan harga yang dicari.
116. Mengecek apakah harga ditemukan pada BST.
117. Menampilkan pesan bahwa harga ditemukan.
118. Jika harga tidak ditemukan.
119. Menampilkan pesan bahwa harga tidak ditemukan.
120. Menangani error jika input bukan angka.
121. Menampilkan pesan input tidak valid.
122. Kosong.
123. Mengecek apakah pengguna memilih menu 3.
124. Menampilkan tulisan daftar harga urut naik.
125. Menampilkan seluruh data BST menggunakan traversal inorder.
126. Membuat pindah baris setelah data ditampilkan.
127. Kosong.
128. Mengecek apakah pengguna memilih menu 4.
129. Menampilkan tulisan preorder.
130. Menampilkan seluruh data BST menggunakan traversal preorder.
131. Membuat pindah baris setelah data ditampilkan.
132. Kosong.
133. Mengecek apakah pengguna memilih menu 5.
134. Menampilkan tulisan postorder.
135. Menampilkan seluruh data BST menggunakan traversal postorder.
136. Membuat pindah baris setelah data ditampilkan.
137. Kosong.
138. Mengecek apakah pengguna memilih menu 6.
139. Menampilkan harga produk paling murah pada BST.
140. Kosong.
141. Mengecek apakah pengguna memilih menu 7.
142. Menampilkan harga produk paling mahal pada BST.
143. Kosong.
144. Mengecek apakah pengguna memilih menu 8.
145. Menampilkan jumlah seluruh produk pada BST.
146. Kosong.
147. Mengecek apakah pengguna memilih menu 9.
148. Menampilkan total seluruh harga produk pada BST.
149. Kosong.
150. Mengecek apakah pengguna memilih menu 10.
151. Menampilkan pesan bahwa program selesai.
152. Kosong.
153. Menangani pilihan menu yang tidak tersedia.
154. Menampilkan pesan pilihan tidak valid.
155. Kosong.
156. Kosong.
157. Mengecek apakah file dijalankan sebagai program utama.
158. Menjalankan fungsi main().


Output Code:

<img width="450" height="671" alt="Screenshot 2026-05-25 211142" src="https://github.com/user-attachments/assets/74d0c9d3-bffe-441f-bd55-9e2305aee9db" />

<img width="431" height="660" alt="Screenshot 2026-05-25 211153" src="https://github.com/user-attachments/assets/8eecf561-68e6-40a6-b9f7-010cc1847fa6" />

<img width="534" height="640" alt="Screenshot 2026-05-25 211203" src="https://github.com/user-attachments/assets/3dc5cd26-ce6f-4fb9-8ae3-dd74ec66ac96" />

<img width="518" height="619" alt="Screenshot 2026-05-25 211211" src="https://github.com/user-attachments/assets/e9aceda0-99b1-41af-b064-1fa1c2200222" />

<img width="483" height="611" alt="Screenshot 2026-05-25 211219" src="https://github.com/user-attachments/assets/12c82988-68ca-4297-9f32-c434b97a0281" />

<img width="488" height="629" alt="Screenshot 2026-05-25 211229" src="https://github.com/user-attachments/assets/e479b8f6-0cef-43ff-8028-3a9150c6cc93" />


Link You Tube:
https://youtu.be/L4TiWH2NyNI






class Node:
    def __init__(self, harga):
        self.key = harga
        self.left = None
        self.right = None

class BSTProduk:
    def __init__(self):
        self.root = None

    def insert_node(self, root, harga):
        if root is None:
            return Node(harga)
        if harga < root.key:
            root.left = self.insert_node(root.left, harga)
        elif harga > root.key:
            root.right = self.insert_node(root.right, harga)
        return root

    def insert(self, harga):
        self.root = self.insert_node(self.root, harga)

    def search_node(self, root, harga):
        if root is None:
            return False
        if root.key == harga:
            return True
        if harga < root.key:
            return self.search_node(root.left, harga)
        return self.search_node(root.right, harga)

    def search(self, harga):
        return self.search_node(self.root, harga)

    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.left)
        print(root.key, end=" ")
        self.inorder(root.right)

    def preorder(self, root):
        if root is None:
            return
        print(root.key, end=" ")
        self.preorder(root.left)
        self.preorder(root.right)

    def postorder(self, root):
        if root is None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.key, end=" ")

    def find_min(self, root):
        if root is None:
            return -1
        current = root
        while current.left is not None:
            current = current.left
        return current.key

    def find_max(self, root):
        if root is None:
            return -1
        current = root
        while current.right is not None:
            current = current.right
        return current.key

    def count_nodes(self, root):
        if root is None:
            return 0
        return 1 + self.count_nodes(root.left) + self.count_nodes(root.right)

    def sum_nodes(self, root):
        if root is None:
            return 0
        return root.key + self.sum_nodes(root.left) + self.sum_nodes(root.right)

def main():
    bst = BSTProduk()
    pilih = 0

    while pilih != 10:
        print("\n=== Data Harga Produk Toko ===")
        print("1. Tambah harga produk")
        print("2. Cari harga produk")
        print("3. Tampilkan harga urut naik (Inorder)")
        print("4. Tampilkan data preorder")
        print("5. Tampilkan data postorder")
        print("6. Harga termurah")
        print("7. Harga termahal")
        print("8. Jumlah produk")
        print("9. Total seluruh harga")
        print("10. Keluar")

        try:
            pilih = int(input("Pilih menu: "))
        except ValueError:
            print("Input tidak valid!")
            continue

        if pilih == 1:
            try:
                x = int(input("Masukkan harga produk: "))
                bst.insert(x)
                print(f"Harga {x} berhasil ditambahkan")
            except ValueError:
                print("Input tidak valid!")

        elif pilih == 2:
            try:
                x = int(input("Cari harga produk: "))
                if bst.search(x):
                    print("Harga ditemukan")
                else:
                    print("Harga tidak ditemukan")
            except ValueError:
                print("Input tidak valid!")

        elif pilih == 3:
            print("Daftar harga urut naik: ", end="")
            bst.inorder(bst.root)
            print()

        elif pilih == 4:
            print("Preorder: ", end="")
            bst.preorder(bst.root)
            print()

        elif pilih == 5:
            print("Postorder: ", end="")
            bst.postorder(bst.root)
            print()

        elif pilih == 6:
            print(f"Harga termurah: {bst.find_min(bst.root)}")

        elif pilih == 7:
            print(f"Harga termahal: {bst.find_max(bst.root)}")

        elif pilih == 8:
            print(f"Jumlah produk: {bst.count_nodes(bst.root)}")

        elif pilih == 9:
            print(f"Total seluruh harga: {bst.sum_nodes(bst.root)}")

        elif pilih == 10:
            print("Program selesai.")

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()

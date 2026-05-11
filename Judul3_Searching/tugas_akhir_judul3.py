def sequential_search(data, n, target):
    i = 0
    counter = 0
    while i < n:
        if data[i] == target:
            counter += 1
        i += 1
    return counter


def main():
    data = ["apel", "mangga", "jeruk", "pisang", "apel",
            "semangka", "melon", "apel", "anggur", "jeruk"]
    n = len(data)

    print(f"Data buah: {data}")

    target = input("Masukkan nama buah yang ingin dicari: ").lower()

    counter = sequential_search(data, n, target)

    if counter > 0:
        print(f"Buah '{target}' ditemukan sebanyak {counter} kali.")
    else:
        print(f"Buah '{target}' tidak ditemukan.")


if __name__ == "__main__":
    main()  
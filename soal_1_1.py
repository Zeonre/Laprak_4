suhu = input("Masukkan suhu tubuh: ")

try:
    suhu = int(suhu)
    if suhu >= 38:
        print("Anda demam")
    else:
        print("Anda tidak demam")
except ValueError:
    print("masukkan suhu dalam bentuk angka")
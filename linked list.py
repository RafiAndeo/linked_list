class Node:
     
    def __init__(self, data):
        self.data = data
        self.next = None
 
class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def push(self, new_data):

        new_node = Node(new_data)

        new_node.next = self.head

        self.head = new_node
        self.count += 1

    def __getitem__(self, index):
        if index > self.count - 1:
            return "Index out of range"
        current_val = self.head
        for n in range(index):
            current_val = current_val.next
        return current_val.data
    
    def __setitem__(self, index, value):
        if index > self.count - 1:
            raise Exception("Index out of range.")
        current = self.head
        for n in range(index):
            current = current.next
        current.data = value
 
    def search(self, x):
 
        current = self.head
 
        while current != None:
            if current.data == x:
                return True
             
            current = current.next
         
        return False

    def searchPrefix(self, x):
        current = self.head
        while current != None:
            if current.data.startswith(x) or current.data.endswith(x):
                return True
            else:
                break
            current = current.next
        return False

def menu():
    print("[1] Tambah data")
    print("[2] Cari data")
    print("[3] Update data")
    print("[4] Cari data secara prefix")
    print("[0] Keluar program")

list = LinkedList()

menu()
option = int(input("Masukkan pilihan menu: "))
count = 0

while option != 0:
    if option == 1:
        nama = str(input("Masukkan nama yang ingin ditambah: "))
        list.push(nama)
        count = count + 1
        print("Data ditambah")
    elif option == 2:
        namaSearch = str(input("Masukkan nama yang ingin dicari: "))
        if list.search(namaSearch):
            print("Data ditemukan")
        else:
            print("Data tidak ditemukan")
    elif option == 3:
        indeksUpdate = int(input("Masukkan indeks ke berapa yang ingin diupdate: "))
        namaGanti = str(input("Masukkan nama yang menjadi update datanya: "))
        list[indeksUpdate] = namaGanti
        print("Data sudah diupdate")
    elif option == 4:
        prefix = str(input("Masukkan prefix yang ingin dicari: "))
        i = 0
        while i < count:
            if list.searchPrefix(prefix):
                print(list[i])
            else:
                print("Data tidak ditemukan")
            i = i + 1
    else:
        print("Pilihan tidak ada")

    print()
    menu()
    option = int(input("Masukkan pilihan menu: "))



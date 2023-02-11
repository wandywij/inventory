from item import Item
from tabulate import tabulate
from state import InputState
from cart import Cart

cart = Cart()

def menu():
    """Fungsi untuk menampilkan daftar tugas.
    """
    print("-"*60)
    print("SELAMAT DATANG DI PERPUSTAKAAN SEDERHANA PACMANN")
    print("-"*60)
    print("1. Input Barang")
    print("2. Hapus Barang")
    print("3. Reset Transaction")
    print("9. Check Order")
    print("0. Exit\n")
    
    choice = int(input('Masukkan Nomor Tugas : '))
    if choice == 1:
        add_item(InputState.NAME, Item(item_name= "", qty= 0, price= 0))
    if choice == 2:
    elif choice == 3:
        cart.reset_transaction()
        print(f"Keranjang anda berhasil dihapus\n {len(cart.items)}")
        menu()
    elif choice == 9:
        check_order()
        menu()



def _check_if_item_already_exist(item_name: str) -> bool:
    if len(cart.items) == 0:
        return False
    count = Item("", 0, 0)
    try:
        count = cart.items[item_name]
    except Exception as e:
        pass
    return count is not None and count.item_name != ""

def add_item(inputState: InputState, item: Item):
    if inputState == InputState.NAME:
        try:
            nama_barang = str(input('Masukkan nama barang : '))
            if _check_if_item_already_exist(nama_barang):
                print("Item sudah ada di keranjang. Silahkan edit quantity nya atau masukkan item lain")
                add_item(inputState, Item(item_name= nama_barang, price= item.price, qty= item.qty))

            add_item(inputState.update_state(inputState), Item(item_name= nama_barang, price= item.price, qty= item.qty))
        except Exception as e:
            print("Telah terjadi kesalahan. Silahkan memilih ulang menu")
            menu()
    elif inputState == InputState.QUANTITY:
        try:
            qty = int(input('Masukkan quantity barang : '))
            add_item(inputState.update_state(inputState), 
                     Item(item_name= item.item_name, price= item.price, qty= qty))
        except Exception as e:
            print("Quantity yang anda masukkan salah. Quantity hanya bisa berupa angka")
            add_item(inputState= inputState)
    elif inputState == InputState.PRICE:
        try:
            price = int(input('Masukkan harga barang : '))
            add_item(inputState.update_state(inputState), 
                     Item(item_name= item.item_name, price= price, qty= item.qty))
        except Exception as e:
            print("Harga yang anda masukkan salah. Harga hanya bisa berupa angka")
            add_item(inputState= inputState)
    elif inputState == InputState.DONE:
        cart.add_item(Item(item_name= item.item_name, qty= item.qty, price= item.price))
        menu()

def check_order():
    try:
        if(len(cart.items) > 0):
            print(tabulate(tabular_data= cart.generate_items(), stralign= "right", headers= ["No", "Nama Item", "Jumlah Item", "Harga/Item", "Total Harga"]))
        else: 
            print("Belum ada belanjaan")
            menu()
    except Exception as e:
        print(f"error checkorder {e}")
        
    
    
        




menu()
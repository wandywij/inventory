from item import Item
from tabulate import tabulate
from state import InputState
from cart import Cart

cart = Cart()

def menu():
    print("-"*60)
    print("Kasirnya Andi")
    print("-"*60)
    print("1. Input Barang")
    print("2. Hapus Barang")
    print("3. Update Barang")
    print("4. Reset Transaction")
    print("9. Check Order")
    print("0. Exit\n")
    
    choice = int(input('Masukkan pilihan anda : '))
    if choice == 1:
        add_item(InputState.NAME, Item(item_name= "", qty= 0, price= 0))
    if choice == 2:
        check_order()
        remove_item()
    elif choice == 3:
        check_order()
        update_item()
    elif choice == 4:
        cart.reset_transaction()
        print(f"Keranjang anda berhasil dihapus\n {len(cart.items)}")
        menu()
    elif choice == 9:
        check_order()
        menu()
    else:
        print("Menu yang anda pilih tidak tersedia")
        menu()



def _check_if_item_already_exist(item_name: str) -> bool:
    if len(cart.items) == 0:
        return False
    count = Item("", 0, 0)
    try:
        count = cart.items.get(item_name.strip().upper())
    except Exception as e:
        pass
    return count is not None and count.item_name != ""

def remove_item():
    item_name = str(input("Masukkan nama barang yang ingin dihapus: "))
    item_is_exist = _check_if_item_already_exist(item_name)
    if item_is_exist:
        cart.remove_items(item_name)
        print(f"Item dengan nama {item_name} berhasil dihapus dari keranjang belanjaan anda")
        print("Keranjang belanja anda: ")
        check_order()
    else: print(f"Item dengan nama {item_name} tidak ditemukan dalam keranjang belanjaan anda")
    menu()

def update_item():
    item_name = str(input("Masukkan nama barang yang ingin diupdate: "))
    item_is_exist = _check_if_item_already_exist(item_name)
    if item_is_exist:
        add_item(InputState.QUANTITY, Item(item_name= item_name, qty=0,price= 0))
    else: 
        print(f"Item dengan nama {item_name} tidak ditemukan dalam keranjang belanjaan anda")
        menu()

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
            add_item(InputState.QUANTITY, Item(item_name= item.item_name, qty= item.qty, price= item.price))
    elif inputState == InputState.PRICE:
        try:
            price = int(input('Masukkan harga barang : '))
            add_item(inputState.update_state(inputState), 
                     Item(item_name= item.item_name, price= price, qty= item.qty))
        except Exception as e:
            print("Harga yang anda masukkan salah. Harga hanya bisa berupa angka")
            add_item(InputState.PRICE, Item(item_name= item.item_name, price= item.price, qty= item.qty))
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
This program is a simple program made for UAS Pacmann.

Tech stacks used :
- Test Driven Development, the code begins with unit test and then the actual code. ex test_cart.py and test_discount_tier.py
- Simple Finite State Machine. When inputting data, user starts from inputting the name and then quantity and then the price. This is to make sure after user input the data, it can only input quantity for the next state.

How to use:
- python cashier.py

Flow of the program :
1. User will be presented with some options. (Input Barang, Hapus Barang, Update Nama Barang, Update Quantity Barang, Update Harga Barang, Reset Transaction, Check Order, Exit)
2. For Input Barang, user will need to input name (string), quantity (int) and price (int). Items will be stored inside a dictionary, because updating or deleting specifiic item will require its name. Dictionary is the best data type for this case.
   The key used for storing inside the dictionary is the item name. if user input "Teh Kotak       ", it will be saved as "Teh Kotak" inside a dictionary with "TEH KOTAK" as key.
3. Hapus Barang, Update Nama Barang, Update quantity Barang, update harga barang will require user to input the name. If the name is incorrect, there will be error message for use.
4. Reset transcation will clear all the item.
5. Check Order is displaying all the items inputted before with the discount if the amount is enough.
6. discount_tier.py store all the discount tier inside a list to enable the app to calculate the discount tier. The list not neccesarily ordered, however on calculation it will be ordered from the code.


Example : 
![alt text](https://github.com/wandywij/inventory/blob/development/assets/image1.png)
![alt text](https://github.com/wandywij/inventory/blob/development/assets/image2.png)
![alt text](https://github.com/wandywij/inventory/blob/development/assets/image3.png)


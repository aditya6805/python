import os
import json
os.system('cls')
inventory = []

def input_inventory(id) -> dict:
    print("Enter product details - ")
    print("*"*20)
    name = input("Enter Product Name - ")
    price = float(input("Enter Price - "))
    quantity = int(input("Enter Quantity - "))
    return {
            "id": id,
            "name": name,
            "price": price,
            "quantity": quantity
            }

inp = int(input("Enter number of producst to be inserted - "))
for id in range(1, inp+1):
    data = input_inventory(id)
    inventory.append(data)

def print_data():
    print(json.dumps(inventory, indent=4))

def update_data():
    inp = input("Do you want to update any data ? (Y/N): ").upper()
    if (inp == 'Y'):
        id = int(input("Enter Product id to be updated: "))
        data = input_inventory(id)
        inventory[id-1] = data
        print_data()

print_data()
update_data()

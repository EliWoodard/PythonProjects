# add item
def AddItem(inventoryList):
    itemName = input("Item name: ")
    itemQuantity = int(input("Item quantity: "))
    itemPrice = float(input("Item price: "))
    inventoryList[itemName] = [itemQuantity, itemPrice]
    print(f"Added {itemQuantity} {itemName} at ${itemPrice} each")

# inventory manager selection
def InventoryHeader():
    print("===== Inventory Manager =====")
    print("1. Add Item")
    print("2. View Inventory")
    print("3. Search Inventory")
    print("4. Exit")
    return int(input("\nChoose an option:"))

# search inventory
def SearchInventory(inventoryList):
    itemKey = input("Enter a existing item name: ")
    inventoryValue = inventoryList[itemKey]
    print(f"Found {itemKey} with quantity of {inventoryValue[0]} at ${inventoryValue[1]} each")


# view inventory
def ViewInventory(inventoryList):
    itemNumber = 1
    for key, value in inventoryList.items():
        print(f"===== {itemNumber} =====")
        print(f"Item: {key}")
        print(f"Quantity: {value[0]}")
        print(f"Price: {value[1]}")
        itemNumber += 1

inventory = {}
userInput = InventoryHeader()
print()

while(userInput != 4):
    if userInput > 4 or userInput < 1:
        print ("Invalid option, please choose between 1 and 4.")
    elif userInput == 1:
        AddItem(inventory)
    elif userInput == 2:
        ViewInventory(inventory)
    elif userInput == 3:
        SearchInventory(inventory)
    elif userInput == 4:
        break
    print()
    userInput = InventoryHeader()
    print()
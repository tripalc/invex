import pickle
from pathlib import Path

def main():

    itemList = []
    
    path_to_file = 'invex.dat'
    path = Path(path_to_file)

    if path.is_file():
        itemList = pickle.load(open("invex.dat", "rb"))
    else:
        print("invex.dat: File not found")
        print("Creating new invex.dat file...")
        pickle.dump(itemList, open("invex.dat", "wb"))
        if path.is_file():
            print("New file created.")
            print("")
            itemList = pickle.load(open("invex.dat", "rb"))
        else:
            print("File couldn't be created. Check if user has write permissions.")
            print("Items created in this invex session will not be saved.")
    
    print("Welcome to invex!")
    choice = 0
    while choice !=7:
        print("Select an action...")
        print("1) Add an item")
        print("2) Delete an item")
        print("3) Modify an item")
        print("4) Search for an item")
        print("5) Sign In")
        print("6) Sign Out")
        print("7) Exit invex")
        choice = int(input())

        if choice == 1:
            print("")
            print("Add an item...")
            newItemN = input("Item Name: ")
            newItemID = input("Scan or type a barcode: ")
            newItemCat = input("Item Category (e.g. Laptop, Cable, etc.): ")
            newItemInOut = ("Signed In")
            itemList.append([newItemN, newItemID, newItemCat, newItemInOut])
            print("Added item",newItemN)
            print("")
            pickle.dump(itemList, open("invex.dat", "wb"))

        elif choice == 2:
            print("")
            print("Delete an item...")
            deleteQ = input("Enter the name/barcode of item to delete: ")
            for item in itemList:
                if deleteQ in item:
                    itemList.remove(item)
                    print("Deleted Item",deleteQ)
                    pickle.dump(itemList, open("invex.dat", "wb"))

        elif choice == 3:
            print("")
            print("Modify an item...")
            modQ = input("Enter the name/barcode of item to modify: ")
            for item in itemList:
                if modQ in item:
                    item[0] = input("New Item Name: ")
                    item[1] = input("Scan or type a new barcode: ")
                    item[2] = input("New Item Category (e.g. Laptop, Cable, etc.): ")
                    print("Modified item",item[0])
                    print("")
                    pickle.dump(itemList, open("invex.dat", "wb"))

        elif choice == 4:
            print("")
            print("Search for an item...")
            searchQ = input("Enter Search Query (* to list all): ")
            for item in itemList:
                if searchQ in item:
                    print(item)
            if searchQ == "*":
                print("List is formatted like this:")
                print("['Name of Item', 'Barcode', 'Category', 'Item Status (In/Out)']")
                print("")
                for i in range(len(itemList)):
                    print(itemList[i])
            print("")

        elif choice == 5:
            print("")
            print("Sign In...")
            InQ = input("Enter the name/barcode of item to Sign In: ")
            for item in itemList:
                if InQ in item:
                    item[3] = "Signed In"
                    pickle.dump(itemList, open("invex.dat", "wb"))
                    print("Signed In",item[0])

        elif choice == 6:
            print("")
            print("Sign Out...")
            OutQ = input("Enter the name/barcode of item to Sign Out: ")
            for item in itemList:
                if OutQ in item:
                    item[3] = "Signed Out"
                    pickle.dump(itemList, open("invex.dat", "wb"))
                    print("Signed Out",item[0])
        
        elif choice == 7:
            print("Exiting invex...")
            print("")

if __name__ == "__main__":
    main()
import os

while True:
    print("\n--- File Automation ---")
    print("1. Create File")
    print("2. Rename File")
    print("3. Delete File")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        filename = input("Enter file name: ")
        open(filename, "w").close()
        print("File created")

    elif choice == "2":
        old = input("Old file name: ")
        new = input("New file name: ")
        os.rename(old, new)
        print("File renamed")

    elif choice == "3":
        filename = input("Enter file name: ")
        os.remove(filename)
        print("File deleted")

    elif choice == "4":
        break

    else:
        print("Invalid choice")
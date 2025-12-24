phone_book = {}

def add_contact():
    name = input("Enter the name: ").strip().lower()
    phone_num = int(input("Enter the phone number: ").strip())
    phone_book[name] = phone_num
    print("------ Contact saved successfully ------")


def read_contact():
    search_name = input("Enter the name to search: ").strip().lower()
    if search_name in phone_book:
        print(f"The number for {search_name} is: {phone_book[search_name]}")
    else:
        print("Contact not found!")


def update_contact():
    update_name = input("Enter the name to update: ").strip().lower()
    if update_name in phone_book:
        update_num = int(input("Enter the new number: "))
        phone_book[update_name] = update_num
        print("--- Contact updated successfully ---")
    else:
        print("Contact not found!")


def delete_contact():
    delete_name = input("Enter the name to delete: ").strip().lower()
    if delete_name in phone_book:
        del phone_book[delete_name]
        print("--- Contact deleted successfully ---")
    else:
        print("Contact not found!")


def main():
    while True:
        print("\nChoose the task:")
        print("""
1. Add contact
2. Read contact
3. Update contact
4. Delete contact
5. Exit
""")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_contact()
        elif choice == 2:
            read_contact()
        elif choice == 3:
            update_contact()
        elif choice == 4:
            delete_contact()
        elif choice == 5:
            print("Exiting phone book...")
            break
        else:
            print("Invalid choice!")


if __name__ == '__main__':
    main()
contacts = {}

while True:
    print("\nContact Book App")
    print("1. Create Contact")
    print("2. View Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Search Contact")
    print("6. Count Contacts")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter name: ")

        if name in contacts:
            print(f"Contact '{name}' already exists.")
        else:
            age = input("Enter age: ")
            email = input("Enter email: ")
            mobile = input("Enter mobile number: ")

            contacts[name] = {
                'age': int(age),
                'email': email,
                'mobile': mobile
            }

            print(f"Contact '{name}' created successfully.")

    elif choice == '2':
        name = input("Enter contact name to view: ")

        if name in contacts:
            contact = contacts[name]

            print(f"\nName: {name}")
            print(f"Age: {contact['age']}")
            print(f"Email: {contact['email']}")
            print(f"Mobile: {contact['mobile']}")
        else:
            print("Contact not found.")

    elif choice == '3':
        name = input("Enter contact name to update: ")

        if name in contacts:
            age = input("Enter updated age: ")
            email = input("Enter updated email: ")
            mobile = input("Enter updated mobile number: ")

            contacts[name] = {
                'age': int(age),
                'email': email,
                'mobile': mobile
            }

            print(f"Contact '{name}' updated successfully.")
        else:
            print("Contact not found.")

    elif choice == '4':
        name = input("Enter contact name to delete: ")

        if name in contacts:
            del contacts[name]
            print(f"Contact '{name}' deleted successfully.")
        else:
            print("Contact not found.")

    elif choice == '5':
        search_name = input("Enter contact name to search: ")

        found = False

        for name, details in contacts.items():
            if search_name.lower() in name.lower():
                print(f"\nName: {name}")
                print(f"Age: {details['age']}")
                print(f"Email: {details['email']}")
                print(f"Mobile: {details['mobile']}")
                found = True

        if not found:
            print("No matching contact found.")

    elif choice == '6':
        print(f"Total contacts: {len(contacts)}")

    elif choice == '7':
        print("Exiting Contact Book...")
        break

    else:
        print("Invalid choice. Please try again.")
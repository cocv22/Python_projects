def display_menu():
    print("""Contact Book Menu:
1. Add Contact
2. View Contact
3. Edit Contact
4. Delete Contact
5. List All Contacts
6. Exit
7. Get the display menu again""")

def add_contact(contact_book):
    name = input("Name for contact: ")
    if name in contact_book:
        print("Contact already exists!")
        return
    try:  
        phone = int(input("Phone number: ").strip())
    except:
        print("Invalid phone number. Please enter a valid integer.")
        return
    email = input("Email address: ")
    address = input("Physical address: ")
    contact_book[name] = {
        "phone": phone,
        "email": email,
        "address": address
    }
    print("Contact added successfully!")

def view_contact(contact_book):
    name = input("Name for contact you want to see: ")
    if name in contact_book:
        print(f"Name: {name}")
        print(f"Phone: {contact_book[name]['phone']}")
        print(f"Email: {contact_book[name]['email']}")
        print(f"Address: {contact_book[name]['address']}")
    else:
        print("Contact not found!")

def edit_contact(contact_book):
    name = input("Name for contact you want to edit: ")
    if name in contact_book:
        try:
            phone = int(input("New phone number (or press Enter to keep current): ").strip() or contact_book[name]['phone'])
            contact_book[name]['phone'] = phone
        except:
            print("Invalid phone number. Please enter a valid integer.")
        email = input("New email address (or press Enter to keep current): ")
        if email:
            contact_book[name]['email'] = email
        address = input("New physical address (or press Enter to keep current): ")
        if address:
            contact_book[name]['address'] = address
        print("Contact updated successfully!")
    
    else:
        print("Contact not found!")

def delete_contact(contact_book):
    name = input("Name of contact you want to delete: ")
    if name in contact_book:
        del contact_book[name]
        print("Contact deleted successfully!")
    
    else:
        print("Contact not found!")

def list_all_contacts(contact_book):
    if contact_book:
        for contact in contact_book:
            print(f"Name: {contact}")
            print(f"Phone: {contact_book[contact]['phone']}")
            print(f"Email: {contact_book[contact]['email']}")
            print(f"Address: {contact_book[contact]['address']}\n")
    else:
        print("No contacts available.")

contact_book = {}
user = 0
display_menu()
while user != 6:
    try:   
        user = int(input("Enter your choice (1-7): "))
    except:
        print("Invalid input. When adding a contact, please enter a valid integer for the phone number.")
        continue
    if user == 1:
        add_contact(contact_book)
    elif user == 2:
        view_contact(contact_book)
    elif user == 3:
        edit_contact(contact_book)
    elif user == 4:
        delete_contact(contact_book)
    elif user == 5:
        list_all_contacts(contact_book)
    elif user == 7:
        display_menu()
    elif user > 7 or user < 1:
        print("Invalid choice. Please try again.")
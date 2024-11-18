contacts = []
def add_contact():
    print("\nAdd New Contact")
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    
    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }
    
    contacts.append(contact)
    print(f"Contact {name} saved successfully")
def view_contacts():
    print("\nContact List:")
    if not contacts:
        print("No contacts found")
    else:
        for contact in contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}")

def search_contact():
    search_term = input("\nEnter name or phone number to search: ")
    found_contacts = [contact for contact in contacts if search_term.lower() in contact['name'].lower() or search_term in contact['phone']]
    
    if not found_contacts:
        print("No matching contacts found.")
    else:
        print("\nSearch Results:")
        for contact in found_contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}")

def update_contact():
    search_term = input("\nEnter the name or phone number of the contact to update: ")
    found_contacts = [contact for contact in contacts if search_term.lower() in contact['name'].lower() or search_term in contact['phone']]
    
    if not found_contacts:
        print("No matching contacts found.")
        return
    
    print("\nSelect the contact to update:")
    for idx, contact in enumerate(found_contacts):
        print(f"{idx+1}. Name: {contact['name']}, Phone: {contact['phone']}")
    
    choice = int(input("\nEnter the number of the contact to update: ")) - 1
    selected_contact = found_contacts[choice]
    print("\nUpdating contact details:")
    selected_contact['name'] = input(f"Enter new name (current: {selected_contact['name']}): ") or selected_contact['name']
    selected_contact['phone'] = input(f"Enter new phone (current: {selected_contact['phone']}): ") or selected_contact['phone']
    selected_contact['email'] = input(f"Enter new email (current: {selected_contact['email']}): ") or selected_contact['email']
    selected_contact['address'] = input(f"Enter new address (current: {selected_contact['address']}): ") or selected_contact['address']
    
    print("Contact updated successfully")

def delete_contact():
    search_term = input("\nEnter the name or phone number to delete: ")
    found_contacts = [contact for contact in contacts if search_term.lower() in contact['name'].lower() or search_term in contact['phone']]
    
    if not found_contacts:
        print("No matching contacts found.")
        return
    
    print("\nSelect the contact to delete:")
    for idx, contact in enumerate(found_contacts):
        print(f"{idx+1}. Name: {contact['name']}, Phone: {contact['phone']}")
    
    choice = int(input("\nEnter the number of the contact to delete: ")) - 1
    selected_contact = found_contacts[choice]
    
    contacts.remove(selected_contact)
    print(f"Contact for {selected_contact['name']} deleted successfully!")

def menu():
    while True:
        print("\n Contact Management System ")
        print("a. Add Contact")
        print("b. View Contacts")
        print("c. Search Contact")
        print("d. Update Contact")
        print("e. Delete Contact")
        print("f. Exit")
        
        choice = input("\nChoose any one option: ")
        
        if choice == "a":
            add_contact()
        elif choice == "b":
            view_contacts()
        elif choice == "c":
            search_contact()
        elif choice == "d":
            update_contact()
        elif choice == "e":
            delete_contact()
        elif choice == "f":
            print(" Goodbye ")
            break
        else:
            print("Invalid  Please retry again.")

if __name__ == "__main__":
    menu()

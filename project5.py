class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        for contact in self.contacts:
            print(f"Name: {contact.name}, Phone: {contact.phone_number}")

    def search_contact(self, search_term):
        matching_contacts = [contact for contact in self.contacts if search_term.lower() in contact.name.lower()]
        if matching_contacts:
            print("Matching contacts:")
            for contact in matching_contacts:
                print(f"Name: {contact.name}, Phone: {contact.phone_number}")
        else:
            print("No matching contacts found.")

    def update_contact(self, name, new_phone_number):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                contact.phone_number = new_phone_number
                print(f"Updated {contact.name}'s phone number to {new_phone_number}.")
                return
        print(f"Contact with name '{name}' not found.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print(f"Deleted contact: {contact.name}")
                return
        print(f"Contact with name '{name}' not found.")

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact = Contact(name, phone, email, address)
            contact_book.add_contact(contact)
            print(f"Added {name} to the contact book.")
        elif choice == "2":
            contact_book.view_contacts()
        elif choice == "3":
            search_term = input("Enter search term (name or phone number): ")
            contact_book.search_contact(search_term)
        elif choice == "4":
            name = input("Enter name of the contact to update: ")
            new_phone = input("Enter new phone number: ")
            contact_book.update_contact(name, new_phone)
        elif choice == "5":
            name = input("Enter name of the contact to delete: ")
            contact_book.delete_contact(name)
        elif choice == "6":
            print("Exiting Contact Book.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
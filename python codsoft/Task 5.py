class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

    def update_contact(self, name=None, phone_number=None, email=None, address=None):
        if name:
            self.name = name
        if phone_number:
            self.phone_number = phone_number
        if email:
            self.email = email
        if address:
            self.address = address

    def __str__(self):
        return f"Name: {self.name}, Phone Number: {self.phone_number}, Email: {self.email}, Address: {self.address}"

class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, contact):
        self.contacts[contact.name] = contact

    def view_contacts(self):
        for contact in self.contacts.values():
            print(contact)

    def search_contact(self, name):
        if name in self.contacts:
            print(self.contacts[name])
        else:
            print("Contact not found.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
        else:
            print("Contact not found.")

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book \n 1. Add Contact \n 2. View Contacts \n 3. Search Contact \n 4. Update Contact \n 5. Delete Contact \n 6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact = Contact(name, phone_number, email, address)
            contact_book.add_contact(contact)
        elif choice == "2":
            contact_book.view_contacts()
        elif choice == "3":
            name = input("Enter name to search: ")
            contact_book.search_contact(name)
        elif choice == "4":
            name = input("Enter name of contact to update: ")
            if name in contact_book.contacts:
                phone_number = input("Enter new phone number: ")
                email = input("Enter new email: ")
                address = input("Enter new address: ")
                contact_book.contacts[name].update_contact(name, phone_number, email, address)
            else:
                print("Contact not found.")
        elif choice == "5":
            name = input("Enter name of contact to delete: ")
            contact_book.delete_contact(name)
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
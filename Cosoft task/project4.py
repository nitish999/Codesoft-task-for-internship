#Contact_book
class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}"


class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email):
        contact = Contact(name, phone, email)
        self.contacts.append(contact)
        print(f"Contact {name} added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            for index, contact in enumerate(self.contacts):
                print(f"{index + 1}. {contact}")

    def update_contact(self, index, name=None, phone=None, email=None):
        if index < 0 or index >= len(self.contacts):
            print("Invalid contact index.")
        else:
            if name:
                self.contacts[index].name = name
            if phone:
                self.contacts[index].phone = phone
            if email:
                self.contacts[index].email = email
            print(f"Contact at index {index + 1} updated successfully.")

    def delete_contact(self, index):
        if index < 0 or index >= len(self.contacts):
            print("Invalid contact index.")
        else:
            removed_contact = self.contacts.pop(index)
            print(f"Contact {removed_contact.name} deleted successfully.")


def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            contact_book.add_contact(name, phone, email)

        elif choice == '2':
            contact_book.view_contacts()

        elif choice == '3':
            contact_book.view_contacts()
            index = int(input("Enter the contact index to update: ")) - 1
            name = input("Enter new name (leave blank to skip): ")
            phone = input("Enter new phone number (leave blank to skip): ")
            email = input("Enter new email (leave blank to skip): ")
            contact_book.update_contact(index, name or None, phone or None, email or None)

        elif choice == '4':
            contact_book.view_contacts()
            index = int(input("Enter the contact index to delete: ")) - 1
            contact_book.delete_contact(index)

        elif choice == '5':
            print("Exiting Contact Book. Goodbye!")
            break

        else:
            print("Invalid choice. Please select again.")


if __name__ == "__main__":
    main()
